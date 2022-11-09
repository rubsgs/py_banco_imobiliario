from models.players.player import Player
from models.properties.property import Property
from turnAction import TurnAction

class Game:
  MAX_TURNS = 1000

  def __init__(self, players: list[Player], properties: dict) -> None:
    self.players = players
    self.activePlayers: list[Player] = []
    for player in players :
      self.activePlayers.append(player)
      
    self.properties = self.makeBoard(properties)
    self.currentTurn = 0
    self.finished = False
    self.timedOut = False
    pass

  def run(self) -> "dict":
    while(not self.finished):
      self.currentTurn += 1
      if(self.currentTurn >= Game.MAX_TURNS): 
        self.finished = True
        self.timedOut = True

      if(not self.finished):
        self.resolveTurn()
    return self.getResults()

  def getResults(self) -> "dict":
    finalBalances = {}
    balanceRanking = []
    #monta um dicionario com os jogadores empataram no saldo final
    #a ordem que os jogadores sao inseridos em cada posicao ja contempla a ordem dos turnos
    for player in self.players:
      if(player.balance not in finalBalances):
        finalBalances[player.balance] = []
      finalBalances[player.balance].append(player) #{saldo:[jogadores, jogadores]}

    #ordena os saldos finais e monta um array com os jogadores
    sortedBalances = sorted(finalBalances, reverse=True)
    for balanceKey in sortedBalances:
      for player in finalBalances[balanceKey]:
        balanceRanking.append(player)
    
    rankingString = ''
    rankingNumber = 1
    for player in balanceRanking:
      rankingString += f'{rankingNumber} - {player.name}:{player.balance} '
      rankingNumber += 1

    return {'ranking': rankingString, 'winner': balanceRanking[0].name, 'timedOut': self.timedOut, 'totalTurns': self.currentTurn}

  def boardSize(self) -> "int":
    return len(self.properties)

  def resolveTurn(self) -> None:
    for player in self.activePlayers:
      nextPosition = player.roll() + player.position
      if(nextPosition >= self.boardSize()):
        player.balance += 100
        nextPosition = nextPosition % self.boardSize()
      player.position = nextPosition

      currentProperty = self.properties[player.position]
      turnAction = player.resolveReturn(currentProperty)
      if(turnAction == TurnAction.BUY_PROPERTY):
        player.balance -= currentProperty.sellValue
        currentProperty.owner = player
        player.ownedProperties.append(currentProperty)
      elif(turnAction == TurnAction.PAY_RENT):
        currentProperty.owner.balance += player.balance if player.balance < currentProperty.rentValue else currentProperty.rentValue
        player.balance -= currentProperty.rentValue
        if(player.balance < 0):
          player.lost = True
          self.activePlayers.remove(player)

    if(len(self.activePlayers) == 1):
      self.finished = True
    pass

  def makeBoard(self, propertyList: dict) -> list[Property]:
    properties = []
    for property in propertyList:
      properties.append(Property(property['sellValue'], property['rentValue']))
    return properties
import json
import random as libRandom
from game import Game
from models.players.impulsive import Impulsive
from models.players.cautious import Cautious
from models.players.random import Random
from models.players.demanding import Demanding
from models.properties.property import Property

maxGames = 300
currentGame = 0

boardFile = open('board.json', 'r')
boardInfo = json.load(boardFile)
boardFile.close()

properties = []
for boardPosition in boardInfo:
  properties.append(Property(boardPosition['sellValue'], boardPosition['rentValue']))

winners = {}
gamesEndedByTimeout = 0
totalTurns = 0
while(currentGame < maxGames):
  currentGame += 1
  players = [Impulsive(), Cautious(), Random(), Demanding()]
  libRandom.shuffle(players)
  game = Game(players, boardInfo)
  gameResult = game.run()

  if gameResult['winner'] not in winners:
    winners[gameResult['winner']] = {'totalVictories': 0, 'percentageVictories': 0}
  winners[gameResult['winner']]['totalVictories'] += 1
  winners[gameResult['winner']]['percentageVictories'] = winners[gameResult['winner']]['totalVictories'] * 100/currentGame
  totalTurns += gameResult['totalTurns']
  if(gameResult['timedOut']):
    gamesEndedByTimeout += 1

averageTurns = "{:.2f}".format(totalTurns/currentGame)
sortedWinners = sorted(winners, key=lambda player: winners[player]['totalVictories'], reverse=True)
print(f'Quantidade de partidas que terminam por time out: {gamesEndedByTimeout}')
print(f'Quantidade média de turnos: {averageTurns}')

print('Porcentagem de vitórias por jogador')
for playerName in winners:
  percentage = "{:.2f}".format(winners[playerName]['percentageVictories'])
  print(f'{playerName}: {percentage}')

print(f'O jogador que mais ganhou foi o {sortedWinners[0]}')
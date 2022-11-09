from models.players.player import Player
from models.properties.property import Property

class Cautious(Player):
  def __init__(self) -> None:
    super().__init__('Cauteloso')

  def wantsToBuyProperty(self, property: Property):
    remainingBalance = self.balance - property.sellValue
    return remainingBalance > 80
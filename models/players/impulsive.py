from models.players.player import Player
from models.properties.property import Property

class Impulsive(Player):
  def __init__(self) -> None:
    super().__init__('Impulsivo')

  def wantsToBuyProperty(self, property: Property):
    return self.balance >= property.sellValue
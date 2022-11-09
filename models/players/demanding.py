from models.players.player import Player
from models.properties.property import Property

class Demanding(Player):
  def __init__(self) -> None:
    super().__init__('Exigente')

  def wantsToBuyProperty(self, property: Property):
    return property.rentValue > 50
from random import random
from models.players.player import Player
from models.properties.property import Property

class Random(Player):
  def __init__(self) -> None:
    super().__init__("Aleatório")

  def wantsToBuyProperty(self, property: Property) -> "bool":
    return random() > 0.5
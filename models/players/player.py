from random import randint
from abc import ABC, abstractmethod
from turnAction import TurnAction
from models.properties.property import Property

class Player(ABC):

  def __init__(self, name) -> None:
    self.name = name
    self.balance = 300
    self.lost = False
    self.ownedProperties = []
    self.position = 0
    return

  def roll(self) -> "int":
    return randint(1,6)

  def resolveReturn(self, property: Property) -> "int":
    if(property.owner and property.owner != self.name):
      return TurnAction.PAY_RENT

    if(property.owner == None and self.wantsToBuyProperty(property)):
      return TurnAction.BUY_PROPERTY

    return TurnAction.PASS

  @abstractmethod
  def wantsToBuyProperty(self, property: Property) -> "bool":
    return



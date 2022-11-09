import json
from random import randint
import sys
from models.properties.property import Property

MAX_POSITIONS = 20
positions = []
for i in range(MAX_POSITIONS):
  sellValue = randint(1, 300)
  rentValue = randint(1, sellValue)
  positions.append({'sellValue': sellValue, 'rentValue':rentValue})

with open('board.json', 'w', encoding='utf-8') as file:
  json.dump(positions, file, ensure_ascii=False, indent=2)
from game.components.enemies.ship import Ship
from game.components.enemies.ship_two import ShipTwo
from game.utils.constants import FPS
import random
class EnemyHandler:
  INTERVAL_BETWEEN_SHIPS = 2 * FPS
  CHOICE_SHIP = ['SHIP_ONE', 'SHIP_TWO']
  SHIP_ONE = 'SHIP_ONE' 
  SHIP_TWO = 'SHIP_TWO'
  def __init__(self):
    self.enemies = []
    self.interval_time = 0

  def update(self):
    if(self.interval_time == self.INTERVAL_BETWEEN_SHIPS):
      if random.choice(self.CHOICE_SHIP)==self.SHIP_ONE:
        self.enemies.append(Ship())
      else:
        self.enemies.append(ShipTwo())
      self.interval_time = 0
    self.interval_time += 1
    for enemy in self.enemies:
      enemy.update()

  def draw(self,sreen):
    for enemy in self.enemies:
      enemy.draw(sreen)
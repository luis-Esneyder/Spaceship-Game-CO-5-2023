from game.components.enemies.ship_red import ShipRed
from game.components.enemies.ship_pink import ShipPink
from game.utils.constants import FPS
import random
class EnemyHandler:
  INTERVAL_BETWEEN_SHIPS = 2 * FPS
  SHIP_RED = 'SHIP_RED' 
  SHIP_PINK = 'SHIP_PINK'
  CHOICE_SHIP = [SHIP_PINK, SHIP_RED]
  ENEMY_MAX = 4
  def __init__(self):
    self.enemies = []
    self.interval_time = 0

  def update(self, bullet_handler):
    self.add_enemy()
    for enemy in self.enemies:
      enemy.update(bullet_handler)
      if not enemy.is_alive:
        self.remove(enemy)

  def draw(self,sreen):
    for enemy in self.enemies:
      enemy.draw(sreen)
  
  def add_enemy(self):
    if(len(self.enemies) < self.ENEMY_MAX ):
      if(self.interval_time == self.INTERVAL_BETWEEN_SHIPS):
        if random.choice(self.CHOICE_SHIP)==self.SHIP_RED:
          self.enemies.append(ShipRed())
        else:
          self.enemies.append(ShipPink())
        self.interval_time = 0
      self.interval_time += 1

  def remove(self, enemy):
    self.enemies.remove(enemy)

  

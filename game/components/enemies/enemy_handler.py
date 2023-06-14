from game.components.enemies.ship import Ship
from game.components.enemies.ship_two import ShipTwo

class EnemyHandler:
  def __init__(self):
    self.enemies = []
    self.enemies.append(Ship())
    self.enemies.append(ShipTwo())

  def update(self):
    for enemy in self.enemies:
      enemy.update()

  def draw(self,sreen):
    for enemy in self.enemies:
      enemy.draw(sreen)
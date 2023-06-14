from game.components.enemies.ship import Ship
class EnemyHandler:
  def __init__(self):
    self.enemies = []
    self.enemies.append(Ship())

  def update(self):
    for enemy in self.enemies:
      enemy.update()

  def draw(self,sreen):
    for enemy in self.enemies:
      enemy.draw(sreen)
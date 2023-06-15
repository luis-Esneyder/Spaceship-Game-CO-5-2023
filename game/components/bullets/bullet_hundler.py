from game.utils.constants import BULLET_ENEMY_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
class BulletHundler:
  def __init__(self):
    self.bullets = []
  
  def update(self):
    for bullet in self.bullets:
      bullet.update()

  def draw(self, screen):
    for bullet in self.bullets:
      bullet.draw(screen)
  
  def add_bullet(self, type, center):
    if(type == BULLET_ENEMY_TYPE):
      self.bullets.append(BulletEnemy(center))

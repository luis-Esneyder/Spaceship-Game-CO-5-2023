from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer
class BulletHundler:
  def __init__(self):
    self.bullets = []
  
  def update(self, player, enemy):
    for bullet in self.bullets:
      if(bullet.type == BULLET_ENEMY_TYPE):
        bullet.update(player)
      elif(bullet.type == BULLET_PLAYER_TYPE):
        bullet.update(enemy)


  def draw(self, screen):
    for bullet in self.bullets:
      bullet.draw(screen)
  
  def add_bullet(self, type, center):
    if(type == BULLET_ENEMY_TYPE):
      self.bullets.append(BulletEnemy(center))
    elif(type == BULLET_PLAYER_TYPE):
      self.bullets.append(BulletPlayer(center))

from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_PLAYER_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_player import BulletPlayer
class BulletHundler:
  def __init__(self):
    self.bullets = []
  
  def update(self, player, handler_enemy, object_enemy_death): #player recive una objeto de SpaceShip  y enemy recibe un objeto de EnemyHandler
    for bullet in self.bullets:
      if(not bullet.show):
        self.bullets.remove(bullet)
      if(bullet.type == BULLET_ENEMY_TYPE):
        bullet.update(player)
      elif(bullet.type == BULLET_PLAYER_TYPE):
        bullet.update(handler_enemy, self.bullets, object_enemy_death)#enemy es un objeto de EnemyHandler

  def draw(self, screen, playing):
    if playing:
      for bullet in self.bullets:
        bullet.draw(screen)
  
  def add_bullet(self, type, center):
    if(type == BULLET_ENEMY_TYPE):
      self.bullets.append(BulletEnemy(center))
    elif(type == BULLET_PLAYER_TYPE):
      self.bullets.append(BulletPlayer(center))
  
  def remove_bullet(self, bullet):
    self.bullets.remove(bullet)

  def reset(self):
    self.bullets = []
from game.utils.constants import BULLET, BULLET_PLAYER_TYPE
from game.components.bullets.bullet import Bullet
import pygame
class BulletPlayer(Bullet):
  WIDTH = 9
  HEIGHT = 32
  SPEED = 7
  def __init__(self, center):
    self.image = BULLET
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
    super().__init__(self.image, center, BULLET_PLAYER_TYPE)

  def update(self, handler_enemy):#un objeto de EnemyHandler contiene un arreglo de enemigos
    self.rect.y -= self.SPEED
    for enemy in handler_enemy.enemies:
      if(self.rect.colliderect(enemy.rect)):
        enemy.is_alive = False
        enemy.is_destroyec = True
        self.show = False
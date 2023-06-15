from game.utils.constants import BULLET, BULLET_PLAYER_TYPE
from game.components.bullets.bullet import Bullet
import pygame
class BulletPlayer(Bullet):
  WIDTH = 9
  HEIGHT = 32
  SPEED = 20
  def __init__(self, center):
    self.image = BULLET
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
    super().__init__(self.image, center, BULLET_PLAYER_TYPE)

  def update(self, enemit):
    if(self.type == BULLET_PLAYER_TYPE):
      self.rect.y -= self.SPEED
      if(self.rect.colliderect(enemit.rect)):
        enemit.is_alive = False
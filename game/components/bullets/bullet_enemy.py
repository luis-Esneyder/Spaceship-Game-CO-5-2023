from game.utils.constants import BULLET_ENEMY
from game.components.bullets.bullet import Bullet
import pygame
class BulletEnemy(Bullet):
  WIDTH = 9
  HEIGHT = 32
  SPEED = 20
  def __init__(self, center):
    self.image = BULLET_ENEMY
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
    super().__init__(self.image, center)

  def update(self, player):
    self.rect.y += self.SPEED
    if(self.rect.colliderect(player.rect)):
      player.is_alive = False
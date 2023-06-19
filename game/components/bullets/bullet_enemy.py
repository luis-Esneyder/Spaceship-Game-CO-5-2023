from game.utils.constants import BULLET_ENEMY, BULLET_ENEMY_TYPE, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet
import pygame
class BulletEnemy(Bullet):
  WIDTH = 9
  HEIGHT = 32
  SPEED = 8
  def __init__(self, center):
    self.image = BULLET_ENEMY
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
    super().__init__(self.image, center, BULLET_ENEMY_TYPE)

  def update(self, player):#recibe un objeto de la clase SpaceShip
    self.rect.y += self.SPEED
    if(self.rect.y >= SCREEN_HEIGHT):
      self.show = False
    if(player.rect.colliderect(self.rect)):
      if not player.has_power and self.show:
        player.resistence -= 1
        if player.resistence == 0:
          player.is_alive = False
      self.show = False

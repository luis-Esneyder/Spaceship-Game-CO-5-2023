import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import SHIP_GRAY
class ShipGray(Enemy):
  
  WIDTH = 40
  HEIGHT = 60
  SPEED_X = 7
  SPEED_Y = 3
  INTERVAL= 30

  def __init__(self):
    self.image = SHIP_GRAY
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL)
  
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import SHIP_BLACK, FPS
class ShipBlack(Enemy):
  
  WIDTH = 50
  HEIGHT = 60
  SPEED_X = 10
  SPEED_Y = 1
  INTERVAL= 500
  INTERVAL_SHOTING_TIME = FPS

  def __init__(self):
    self.image = SHIP_BLACK
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL, self.INTERVAL_SHOTING_TIME)
  
from game.components.enemies.enemy import Enemy
from game.utils.constants import SHIP_RED, FPS
import pygame
class ShipRed(Enemy):

  WIDTH = 40
  HEIGHT = 60
  SPEED_X = 5
  SPEED_Y = 1
  INTERVAL = 50
  INTERVAL_SHOTING_TIME =  (FPS/2) * 3
  TIPE='SHIP_RED'
  def __init__(self):
    self.image = SHIP_RED
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL, self.INTERVAL_SHOTING_TIME, self.TIPE)
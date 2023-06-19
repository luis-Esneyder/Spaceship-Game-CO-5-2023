from game.components.enemies.enemy import Enemy
from game.utils.constants import SHIP_GOD, SCREEN_WIDTH, FPS
import pygame
class ShipGod(Enemy):

  WIDTH = 100
  HEIGHT = 100
  SPEED_X = 15
  SPEED_Y = 0
  INTERVAL = SCREEN_WIDTH
  INTERVAL_SHOTING_TIME = FPS//2
  POINT = 15
  ENDURANCE=25
  TYPE = 'SHIP_GOD'
  def __init__(self):
    self.image = SHIP_GOD
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL, self.INTERVAL_SHOTING_TIME,self.TYPE ,self.POINT, self.ENDURANCE)

  
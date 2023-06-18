from game.components.enemies.enemy import Enemy
from game.utils.constants import MALEVOLO_CUCARACHON, SCREEN_WIDTH, FPS
import pygame
class MalevoloCucarachon(Enemy):

  WIDTH = 70
  HEIGHT = 100
  SPEED_X = 15
  SPEED_Y = 2
  INTERVAL = SCREEN_WIDTH
  INTERVAL_SHOTING_TIME = FPS//2
  POINT = 5
  ENDURANCE=10
  TYPE = 'malevolo_cucarachon'
  def __init__(self):
    self.image = MALEVOLO_CUCARACHON
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL, self.INTERVAL_SHOTING_TIME,self.TYPE ,self.POINT, self.ENDURANCE)

    
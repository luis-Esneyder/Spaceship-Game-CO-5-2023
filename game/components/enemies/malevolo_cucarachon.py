from game.components.enemies.enemy import Enemy, SCREEN_WIDTH
from game.utils.constants import MALEVOLO_CUCARACHON
import pygame
class MalevoloCucarachon(Enemy):

  WIDTH = 70
  HEIGHT = 100
  SPEED_X = 25
  SPEED_Y = 3
  INTERVAL = SCREEN_WIDTH

  def __init__(self):
    self.image = MALEVOLO_CUCARACHON
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL)
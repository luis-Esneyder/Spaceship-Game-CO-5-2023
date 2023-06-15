from game.components.enemies.enemy import Enemy, SCREEN_WIDTH
from game.utils.constants import DRAGON
import pygame
class Dragon(Enemy):

  WIDTH = 50
  HEIGHT = 70
  SPEED_X = 25
  SPEED_Y = 3
  INTERVAL = SCREEN_WIDTH

  def __init__(self):
    self.image = DRAGON
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL)
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1
import pygame
class Ship(Enemy):

  WIDTH = 40
  HEIGHT = 60
  SPEED_X = 5
  SPEED_Y = 2
  INTERVAL = 50

  def __init__(self):
    self.image = ENEMY_1
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL)
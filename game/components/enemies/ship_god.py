from game.components.enemies.enemy import Enemy
from game.utils.constants import SHIP_GOD, SCREEN_WIDTH, FPS
import pygame
import math
class ShipGod(Enemy):

  WIDTH = 100
  HEIGHT = 100
  SPEED_X = 5
  SPEED_Y = 1
  INTERVAL = SCREEN_WIDTH
  INTERVAL_SHOTING_TIME = FPS//2
  POINT = 15
  ENDURANCE=25
  AMPLITUDE = 20
  FREQUENCY = 0.1
  TYPE = 'SHIP_GOOD'
  def __init__(self):
    self.image = SHIP_GOD
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
    super().__init__(self.image, self.SPEED_X, self.SPEED_Y, self.INTERVAL, self.INTERVAL_SHOTING_TIME,self.TYPE ,self.POINT, self.ENDURANCE)

  def move(self):
    move_seno = self.AMPLITUDE * math.sin(self.FREQUENCY * self.index)
    self.rect.y += self.SEEP_Y + move_seno
    super().move() 

    
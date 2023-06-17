import pygame
import random
from game.utils.constants import SCREEN_WIDTH
class Power:
  WIDTH = 30
  HEIGHT = 30
  def __init__(self, image, type) :
    self.image = image  
    self.type = type   
    self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))  
    self.rect = self.image.get_rect()
    self.rect.x = random.randint(120, SCREEN_WIDTH -120)
    self.rect.y = 0

  def update(self):
    self.rect.y += 10 

  def draw(self, screen):
    screen.blit(self.image, self.rect)

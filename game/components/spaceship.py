import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT
class Spaceship:
  X_POST = (SCREEN_WIDTH//2) - 40
  Y_POST = 500
  def __init__(self):
    self.image = SPACESHIP
    self.image = pygame.transform.scale(self.image,(40,60))
    self.rect = self.image.get_rect()
    self.rect.x = self.X_POST
    self.rect.y = self.Y_POST
  
  def update(self, user_input):
    if user_input[pygame.K_LEFT]:
      self.move_left()
    elif user_input[pygame.K_RIGHT]:
      self.move_right()
    elif user_input[pygame.K_UP]:
      pass

  def draw(self, screen):
    screen.blit(self.image, self.rect)  
  
  def move_left(self):
    if self.rect.left > 0:
      self.rect.x -=10
  
  def move_right(self):
    if self.rect.right < SCREEN_WIDTH:
      self.rect.x +=10
  
  def move_up(self):
    if self.rect.up < SCREEN_HEIGHT:
      self.rect.x -=10

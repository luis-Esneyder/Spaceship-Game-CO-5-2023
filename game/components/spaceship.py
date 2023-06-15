import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT
class Spaceship:
  WIDTH = 40
  HEIGTH = 60
  X_POST = (SCREEN_WIDTH//2) - WIDTH
  Y_POST = 500
  def __init__(self):
    self.image = SPACESHIP
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGTH))
    self.rect = self.image.get_rect()
    self.rect.x = self.X_POST
    self.rect.y = self.Y_POST
    self.is_alive = True
  
  def update(self, user_input, speed):
    if user_input[pygame.K_LEFT]:
      self.move_left(speed)
    elif user_input[pygame.K_RIGHT]:
      self.move_right(speed)
    elif user_input[pygame.K_UP]:
      self.move_up(speed)
    elif user_input[pygame.K_DOWN]:
      self.move_down(speed)

  def draw(self, screen):
    screen.blit(self.image, self.rect)  
  
  def move_left(self, speed):
    self.rect.x -=speed
    if self.rect.left <= self.WIDTH//2:
      self.rect.x = SCREEN_WIDTH - self.WIDTH//2
    
  def move_right(self, speed):
    self.rect.x +=speed
    if self.rect.right >= SCREEN_WIDTH + self.WIDTH//2:
      self.rect.x = - self.WIDTH//2
  
  def move_up(self,speed):
    if self.rect.y > SCREEN_HEIGHT//2:
      self.rect.y -=speed

  def move_down(self, speed):
    if self.rect.y < SCREEN_HEIGHT-60:
      self.rect.y +=speed
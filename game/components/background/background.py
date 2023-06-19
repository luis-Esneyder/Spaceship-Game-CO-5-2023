from game.utils.constants import BG, SCREEN_HEIGHT, SCREEN_WIDTH, BG_START
import pygame
class Background:
  def __init__(self, image = BG):
    self.image =  image
    self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    self.y_pos_bg = 0
    self.x_pos_bg = 0
    self.game_speed = 10

  def update(self):
    self.y_pos_bg += self.game_speed

  def draw(self, screen, playing):
    self.draw_background(screen, playing)
    self.draw_bacground_start(screen, playing)

  def draw_background(self, screen, playing):
    if playing:
      image_height = self.image.get_height()
      screen.blit(self.image, (self.x_pos_bg, self.y_pos_bg))
      screen.blit(self.image, (self.x_pos_bg, self.y_pos_bg - image_height))
      if self.y_pos_bg >= SCREEN_HEIGHT:
        screen.blit(self.image, (self.x_pos_bg, self.y_pos_bg - image_height))
        self.y_pos_bg = 0

  def draw_bacground_start(self, screen, playin):
    if not playin:
      image = BG_START
      image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
      screen.blit(image, (0,0))

  def reset(self):
    self.game_speed = 10

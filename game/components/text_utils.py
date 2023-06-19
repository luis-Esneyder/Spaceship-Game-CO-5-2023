from pygame.font import Font
import pygame
from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT

def get_message(message, size, color, width= SCREEN_WIDTH//2, height= SCREEN_HEIGHT//2):
  font = Font(FONT_STYLE, size)
  text =  font.render(message, True, color)
  text_rect = text.get_rect()
  text_rect.center = (width, height)
  return  text, text_rect
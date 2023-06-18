from game.utils.constants import SCREEN_WIDTH, TEXT_SHOW_SCORE, SIZE_NORMAL_TEXT, WHITE_COLOR
from game.components import text_utils
class Statistic:
  def __init__(self):
    self.score = 0
    self.max_score = 0
    self.number_death = 0

  def update(self, number_enemy):
    self.score = number_enemy
    if(self.score > self.max_score):
      self.max_score = self.score

  def draw(self, screen, playing):
    if playing:
      self.draw_score(screen)

  def draw_score(self, screen):
    score, score_rect = text_utils.get_message(TEXT_SHOW_SCORE.format(self.score), SIZE_NORMAL_TEXT ,WHITE_COLOR, SCREEN_WIDTH - 100 ,  20 )
    screen.blit(score, score_rect)
  
  def reset(self):
    self.score = 0
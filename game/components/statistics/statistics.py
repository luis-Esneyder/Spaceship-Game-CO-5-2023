from game.utils.constants import SCREEN_WIDTH, TEXT_SHOW_SCORE, SIZE_NORMAL_TEXT, TEXT_COLOR, SCREEN_HEIGHT, TEXT_SHOW_DEATH, TEXT_SHOW_MAXSCORE
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
    self.draw_score(screen, playing)
    self.draw_number_death(screen, playing)

  def draw_score(self, screen , playing):
    if playing:
      score, score_rect = text_utils.get_message(TEXT_SHOW_SCORE.format(self.score), SIZE_NORMAL_TEXT ,TEXT_COLOR, SCREEN_WIDTH - 100 ,  20 )
      screen.blit(score, score_rect)
    elif self.number_death > 0:
      score, score_rect = text_utils.get_message(TEXT_SHOW_SCORE.format(self.score), SIZE_NORMAL_TEXT , TEXT_COLOR,SCREEN_WIDTH//2,  SCREEN_HEIGHT//2 + 40 )
      max_score, max_score_rect = text_utils.get_message(TEXT_SHOW_MAXSCORE.format(self.max_score), SIZE_NORMAL_TEXT , TEXT_COLOR,SCREEN_WIDTH//2,  SCREEN_HEIGHT//2 + 65 )
      screen.blit(score, score_rect)
      screen.blit(max_score, max_score_rect)

  def draw_number_death(self, screen , playing):
    if not playing and self.number_death > 0:
      number_death, number_death_rect = text_utils.get_message(TEXT_SHOW_DEATH.format(self.number_death), SIZE_NORMAL_TEXT , TEXT_COLOR,SCREEN_WIDTH//2,  SCREEN_HEIGHT//2 + 90)
      screen.blit(number_death, number_death_rect)

  def reset(self):
    self.score = 0
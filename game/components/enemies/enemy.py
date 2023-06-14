import random
from game.utils.constants import SCREEN_WIDTH
class Enemy:
  X_POS_LIST = [50, 100, 150, 200, 250 , 300, 350, 400, 450, 500]
  Y_POS = 20
  LEFT= 'left'
  RIGHT= 'right'
  MOV_X = [LEFT, RIGHT]

  def __init__(self, image, speed_x:int, speed_y:int, interval):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = random.choice(self.X_POS_LIST)
    self.rect.y = self.Y_POS
    self.mov_x = random.choice(self.MOV_X)
    self.index = 0
    self.SEEP_X = speed_x
    self.SEEP_Y = speed_y
    self.INTERVAL = interval

  def update(self):
    self.rect.y += self.SEEP_Y
    if self.mov_x == self.LEFT:
      self.rect.x -= self.SEEP_X
      if self.index > self.INTERVAL or self.rect.x <=0:
        self.mov_x = self.RIGHT
        self.index = 0
    else:
      self.rect.x += self.SEEP_X
      if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
        self.mov_x = self.LEFT
        self.index = 0
    self.index +=1

  def draw(self, screen):
    screen.blit(self.image, self.rect)
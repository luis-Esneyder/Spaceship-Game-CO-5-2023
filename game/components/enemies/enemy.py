import random
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_ENEMY_TYPE
class Enemy:
  X_POS_LIST = [i for i in range(50, SCREEN_WIDTH, 50)]
  Y_POS = 20
  LEFT= 'left'
  RIGHT= 'right'
  MOV_X = [LEFT, RIGHT]

  def __init__(self, image, speed_x:int, speed_y:int, interval:int, interval_shoting_time, get_point=1,  endurance=1):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = random.choice(self.X_POS_LIST)
    self.rect.y = self.Y_POS
    self.mov_x = random.choice(self.MOV_X)
    self.index = 0
    self.SEEP_X = speed_x
    self.SEEP_Y = speed_y
    self.interval = interval
    self.is_alive = True
    self.shooting_time = 0
    self.interval_shoting_time = interval_shoting_time
    self.is_destroyec = False
    self.get_point = get_point
    self.endurance = endurance

  def update(self, bullet_handler):
    if(self.rect.y >= SCREEN_HEIGHT):
      self.is_alive = False
    self.shooting_time += 1
    self.move()
    self.shoot(bullet_handler)


  def draw(self, screen):
    screen.blit(self.image, self.rect)

  def move(self):
    self.rect.y += self.SEEP_Y
    if self.mov_x == self.LEFT:
      self.rect.x -= self.SEEP_X
      if self.index > self.interval or self.rect.x <=0:
        self.mov_x = self.RIGHT
        self.index = 0
    else:
      self.rect.x += self.SEEP_X
      if self.index > self.interval or self.rect.x >= SCREEN_WIDTH - self.rect.width:
        self.mov_x = self.LEFT
        self.index = 0
    self.index +=self.SEEP_X
  def shoot(self, bullet_handler):
    if self.shooting_time % self.interval_shoting_time == 0:
      bullet_handler.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)

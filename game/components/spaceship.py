import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_PLAYER_TYPE, DEFAULT_TYPE, WHITE_COLOR, HEART, SHOOT_PLAYER
from game.components import text_utils
class Spaceship:
  WIDTH = 40
  HEIGTH = 60
  WIDTH_HEART = 25
  HEIGTH_HEART = 25
  X_POST = (SCREEN_WIDTH//2) - WIDTH
  Y_POST = 500
  VOLUMENT_MUSIC = 0.6
  def __init__(self):
    self.image = SPACESHIP
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGTH))
    self.rect = self.image.get_rect()
    self.rect.x = self.X_POST
    self.rect.y = self.Y_POST
    self.is_alive = True
    self.power_type = DEFAULT_TYPE
    self.has_power = False
    self.power_time = 0
    self.resistence = 2
    self.contador = 0
    self.music_shot = SHOOT_PLAYER
  
  def update(self, user_input, speed, bullet_handler):
    self.contador+=1
    if user_input[pygame.K_LEFT]:
      self.move_left(speed)
    elif user_input[pygame.K_RIGHT]:
      self.move_right(speed)
    elif user_input[pygame.K_UP]:
      self.move_up(speed)
    elif user_input[pygame.K_DOWN]:
      self.move_down(speed)
    elif user_input[pygame.K_SPACE]:
      self.shoot(bullet_handler)

  def draw(self, screen, playing):
    if playing:
      screen.blit(self.image, self.rect)  
      self.draw_power_time(screen)
      self.draw_live_heart(screen)
  
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
  
  def shoot(self, bullet_handler):
    if(self.contador % 3 == 0 ):
      self.music_shot.play()
      self.music_shot.set_volume(self.VOLUMENT_MUSIC)
      bullet_handler.add_bullet(BULLET_PLAYER_TYPE, self.rect.center)

  def set_power_image(self, image):
    self.image = image
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGTH))

  def set_default_image(self):
    self.image = SPACESHIP
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGTH))
  
  def draw_power_time(self, screen):
    if self.has_power:
      power_time = round((self.power_time - pygame.time.get_ticks())/1000, 2)
      if power_time>=0:
        text, text_rect = text_utils.get_message(f'{self.power_type.capitalize()} is enable for {power_time}', 20 ,WHITE_COLOR, 150, 50)
        screen.blit(text, text_rect)
      else:
        self.has_power = False
        self.power_time = DEFAULT_TYPE
        self.set_default_image()

  def draw_live_heart(self, screen, image= HEART):
    image = image
    image_rect = image.get_rect()
    image_rect.x = 0
    image_rect.y = SCREEN_HEIGHT - self.HEIGTH_HEART
    for i in range(self.resistence):
      image = pygame.transform.scale(image, (self.WIDTH_HEART,self.HEIGTH_HEART))
      screen.blit(image, image_rect)
      image_rect.x += self.WIDTH_HEART


  def reset(self):
    self.rect.x = self.X_POST
    self.rect.y = self.Y_POST
    self.resistence=1
    self.is_alive = True
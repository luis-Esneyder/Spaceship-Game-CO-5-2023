from game.components.power.shield import Shield
from game.components.power.heart import Heart
from game.utils.constants import SPACESHIP_SHIELD, SCREEN_HEIGHT, SHIELD_TYPE, HEART_TYPE, ABSOR_HEAR, ABSOR_SHIELD
import random
import pygame
class PowerHandler:
  WHEN_APPEARS_SHIELD = random.randint(3000, 7000)  
  TYPE = 'malevolo_cucarachon'
  def __init__(self):
    self.powers = []
    self.score_ref_power = 0
    self.score_ref_heard = 0
    self.music_absor_heart = ABSOR_HEAR
    self.music_absor_shield =  ABSOR_SHIELD
  def update(self, player, score, enemies):
    self.generate_power(score)
    self.generate_heart(enemies)
    for power in self.powers:
      self.remove(power)
      self.power_death(power)
      power.update()
      self.colliderect_power(power, player)
      self.colliderect_heart(power, player, score)

  def draw(self, screen, playing):
    if playing:
      for power in self.powers:
        power.draw(screen )

  def colliderect_power(self, power, player):
    if(power.type == SHIELD_TYPE):  
      if power.rect.colliderect(player.rect):
        self.music_absor_shield.play()
        pygame.time.delay(50)
        power.start_time = pygame.time.get_ticks()
        power.is_alive = False
        player.power_type = power.type
        player.has_power = True
        player.power_time = power.start_time + (power.duration * 1000)
        player.set_power_image(SPACESHIP_SHIELD)

  def generate_power(self, score):
    if(score - self.score_ref_power > 10):
      power = Shield()
      self.powers.append(power)
      self.WHEN_APPEARS_SHIELD += random.randint(3000, 7000)
      self.score_ref_power = score

  def colliderect_heart(self, power, player, score):
    if(power.type == HEART_TYPE and power.is_alive):  
      if power.rect.colliderect(player.rect):
        self.music_absor_heart.play()
        pygame.time.delay(50)
        if player.is_alive and power.is_alive:
          if player.resistence<3:
            player.resistence +=1
          power.is_alive = False
          self.score_ref_heard = score
        
  def generate_heart(self, enemies):
      for enemy  in enemies:
        if enemy.type == self.TYPE and enemy.is_destroyec:
          heart = Heart()
          self.powers.append(heart)

  def remove(self, power):
    if not power.is_alive:
      self.powers.remove(power)

  def power_death(self, power):
    if power.rect.y == SCREEN_HEIGHT:
      power.is_alive = False

  def reset(self):
    self.powers = []
    self.score_ref = 0
from game.components.power.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD, SCREEN_HEIGHT
import random
import pygame
class PowerHandler:
  WHEN_APPEARS_SHIELD = random.randint(3000, 7000)  
  def __init__(self):
    self.powers = []
    self.score_ref = 0

  def update(self, player, score):
    if(len(self.powers) == 0 and  score - self.score_ref > 5):
      self.generate_power()
      self.score_ref = score
    for power in self.powers:
      self.remove(power)
      self.power_death(power)
      power.update()
      self.colliderect_power(power, player)

  def draw(self, screen):
    for power in self.powers:
      power.draw(screen)

  def colliderect_power(self, power, player):
    if player.rect.colliderect(power.rect):
      power.start_time = pygame.time.get_ticks()
      power.is_alive =False
      player.power_type = power.type
      player.has_power = True
      player.power_time = power.start_time + (power.duration * 1000)
      player.set_power_image(SPACESHIP_SHIELD)

  def generate_power(self):
    power = Shield()
    self.powers.append(power)
    self.WHEN_APPEARS_SHIELD += random.randint(3000, 7000)

  def remove(self, power):
    if not power.is_alive:
      self.powers.remove(power)

  def power_death(self, power):
    if power.rect.y == SCREEN_HEIGHT:
      power.is_alive = False

  def reset(self):
    self.powers = []
    self.score_ref = 0
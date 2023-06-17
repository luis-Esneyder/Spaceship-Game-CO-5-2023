from game.components.power.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD
import random
import pygame
class PowerHandler:
  
  def __init__(self) -> None:
    self.powers = []
    self.when_appears = random.randint(3000, 7000)
    self.duration = random.randint(3, 5)

  def update(self, player):
    current_time = pygame.time.get_ticks()
    if(len(self.powers) == 0 or current_time >= self.when_appears):
      self.generate_power()
    for power in self.powers:
      power.update()
      if player.rect.colliderect(power.rect):
        power.start_time = pygame.time.get_ticks()
        player.power_type = power.type
        player.has_power = True
        player.power_time = power.start_time + (self.duration * 1000)
        player.set_power_image(SPACESHIP_SHIELD)

  def draw(self, screen):
    for power in self.powers:
      power.draw(screen)

  def generate_power(self):
    power = Shield()
    self.powers.append(power)
    self.when_appears += random.randint(3000, 7000)

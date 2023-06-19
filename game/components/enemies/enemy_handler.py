from game.components.enemies.ship_red import ShipRed
from game.components.enemies.ship_gray import ShipGray
from game.components.enemies.ship_black import ShipBlack
from game.components.enemies.malevolo_cucarachon import MalevoloCucarachon
from game.utils.constants import FPS
import random
class EnemyHandler:
  INTERVAL_BETWEEN_SHIPS_DEFAULT =  FPS
  INTERVAL_BETWEEN_SHIPS_MORE_DIFFICULT =  4 * FPS
  SHIP_RED = 'SHIP_RED' 
  SHIP_PINK = 'SHIP_PINK'
  SHIP_BLACK = 'SHIP_BLACK'
  LIST_SHIP = [SHIP_PINK, SHIP_RED, SHIP_BLACK]
  ENEMY_MAX = 4
  def __init__(self):
    self.enemies = []
    self.interval_time = 1
    self.number_enemy_destroyec = 0

  def update(self, bullet_handler, player, score):
    self.add_enemy(score)
    for enemy in self.enemies:
      self.colliderect_player(enemy, player)
      if enemy.is_destroyec:
        self.number_enemy_destroyec += enemy.get_point
      enemy.update(bullet_handler)
      self.remove(enemy)  

  def draw(self,sreen, playing):
    if playing:
      for enemy in self.enemies:
        enemy.draw(sreen)
  
  def add_enemy(self, score):
    if(len(self.enemies) < self.ENEMY_MAX ):
      if(self.interval_time % self.INTERVAL_BETWEEN_SHIPS_DEFAULT == 0):
        chice_ship = random.choice(self.LIST_SHIP)
        if chice_ship==self.SHIP_RED:
          self.enemies.append(ShipRed())
        elif chice_ship == self.SHIP_PINK:
          self.enemies.append(ShipGray())
        elif chice_ship == self.SHIP_BLACK:
          self.enemies.append(ShipBlack())
    if(score > 10 and self.interval_time % self.INTERVAL_BETWEEN_SHIPS_MORE_DIFFICULT == 0):
      self.enemies.append(MalevoloCucarachon())
    self.interval_time += 1

  def remove(self, enemy):
    if not enemy.is_alive:
      self.enemies.remove(enemy)
  
  def colliderect_player(self,enemy, player):
    if(enemy.rect.colliderect(player.rect)):
      if not player.has_power:
        self.enemies.remove(enemy)
        player.resistence -= 1
        if player.resistence == 0:
          player.is_alive = False

  def reset(self):
    self.enemies = []
    self.number_enemy_destroyec = 0
    self.interval_time = 1

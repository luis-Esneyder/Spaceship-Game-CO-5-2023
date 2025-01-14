from game.utils.constants import BULLET, BULLET_PLAYER_TYPE, BULLET_ENEMY_TYPE
from game.components.bullets.bullet import Bullet
import pygame
class BulletPlayer(Bullet):
  WIDTH = 9
  HEIGHT = 32
  SPEED = 7
  TYPE = 'malevolo_cucarachon'
  def __init__(self, center):
    self.image = BULLET
    self.image = pygame.transform.scale(self.image,(self.WIDTH, self.HEIGHT))
    super().__init__(self.image, center, BULLET_PLAYER_TYPE)

  def update(self, handler_enemy, bullets, object_enemy_death):#un objeto de EnemyHandler contiene un arreglo de enemigos
    self.rect.y -= self.SPEED
    if(self.rect.y <= 0):
      self.show = False
    self.kill_enemy(handler_enemy.enemies, object_enemy_death)
    for bullet in bullets:
      if self.rect.colliderect(bullet.rect):
        if(bullet.type == BULLET_ENEMY_TYPE):
          bullet.show = False
          self.show = False
    
  def kill_enemy(self, enemies, object_enemy_death):
    for enemy in enemies:
      if(self.rect.colliderect(enemy.rect)):
        enemy.resistence -=1
        if(enemy.resistence == 0):
          enemy.music_death.play()
          enemy.music_death.set_volume(0.6)
          enemy.is_alive = False
          enemy.is_destroyec= True
        self.generator_object(enemy, object_enemy_death, enemy.is_destroyec)
        self.show = False
    
  def generator_object(self, enemy, object_enemy_death, enemy_destroyec):
    if enemy_destroyec:  
      if ( not enemy.type in object_enemy_death):
        object_enemy_death.update({enemy.type: 1})
      else:
        object_enemy_death[enemy.type] +=1 


import pygame
import os
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_hundler import BulletHundler
from game.components.power.power_handler import PowerHandler
from game.components.background.background import Background
from game.components.statistics.statistics import Statistic
from game.components import text_utils
from game.utils.constants import ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SIZE_TITLE, MUSIC_START, TEXT_COLOR, SHIP_DESTROYEC,GAME_OVER
class Game:
    INCREMENT_VEL = 1
    INTERVAL_INCREMENT_VEL = 6 * FPS
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.background = Background()
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()#enimies = []
        self.bullet_handler = BulletHundler()
        self.power_handler = PowerHandler()
        self.statistic = Statistic()
        self.contador = 0
        self.music = MUSIC_START
        self.music.play(-1)
        self.music.set_volume(0.2)
        self.music_death = SHIP_DESTROYEC
    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()

    def update(self):
        self.background.update()
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.game_speed, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler, self.player, self.statistic.score)
            self.bullet_handler.update(self.player, self.enemy_handler)#player:SpaceShip, enemy_handler: EnemyHandler //que contiene enemies=[]
            self.power_handler.update(self.player, self.statistic.score, self.enemy_handler.enemies)
            self.statistic.update(self.enemy_handler.number_enemy_destroyec)
            self.contador+=1
            if(not self.player.is_alive):
                self.music_death.play()
                self.music_death.set_volume(1)
                pygame.time.delay(500)
                self.playing = False
                self.statistic.number_death +=1
            if self.contador % self.INTERVAL_INCREMENT_VEL == 0:
                self.background.game_speed += self.INCREMENT_VEL
    def draw(self):
        self.background.draw(self.screen, self.playing, self.statistic.number_death)
        self.player.draw(self.screen, self.playing)
        self.clock.tick(FPS)
        self.enemy_handler.draw(self.screen, self.playing)
        self.bullet_handler.draw(self.screen, self.playing)
        self.power_handler.draw(self.screen, self.playing)
        self.statistic.draw(self.screen, self.playing)
        self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_menu(self):
        if not self.playing:
            if self.statistic.number_death == 0:
                text, text_rect = text_utils.get_message('WELCOME TO THE GAME', 30 ,TEXT_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
                text_2, text_rect_2 = text_utils.get_message('Press any key to start', 30 ,TEXT_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT//1.7)
                self.screen.blit(text, text_rect)
                self.screen.blit(text_2, text_rect_2)
            else:
                image = GAME_OVER
                image_rect = image.get_rect()
                image_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//3)
                text, text_rect = text_utils.get_message('PRESS ANY KEY TO START', SIZE_TITLE , TEXT_COLOR, SCREEN_WIDTH//2, SCREEN_HEIGHT - 80 )
                self.screen.blit(text, text_rect)
                self.screen.blit(image, image_rect)

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_handler.reset()
        self.statistic.reset()
        self.background.reset()
        self.game_speed = 10
        self.contador = 0
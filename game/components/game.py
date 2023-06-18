import pygame
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_hundler import BulletHundler
from game.components.power.power_handler import PowerHandler
from game.components import text_utils
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, SIZE_TITLE, SIZE_NORMAL_TEXT, TEXT_SHOW_SCORE
from game.utils.constants import TEXT_SHOW_DEATH, TEXT_SHOW_MAXSCORE, DEFAULT_TYPE
class Game:

    INCREMENT_VEL = 2
    INTERVAL_INCREMENT_VEL = 10 * FPS
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()#enimies = []
        self.bullet_handler = BulletHundler()
        self.power_handler = PowerHandler()
        self.score = 0
        self.max_score = 0
        self.number_death = 0
        self.contador = 0
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
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.player.update(user_input, self.game_speed, self.bullet_handler)
            self.enemy_handler.update(self.bullet_handler, self.player, self.score)
            self.bullet_handler.update(self.player, self.enemy_handler)#player:SpaceShip, enemy_handler: EnemyHandler //que contiene enemies=[]
            self.power_handler.update(self.player, self.score)
            self.get_score()
            self.contador+=1
            if(not self.player.is_alive):
                pygame.time.delay(300)
                self.playing = False
                self.number_death +=1
            if self.contador % self.INTERVAL_INCREMENT_VEL == 0:
                self.game_speed += self.INCREMENT_VEL
    def draw(self):
        self.draw_background()
        if self.playing:
            self.clock.tick(FPS)
            self.player.draw(self.screen)
            self.enemy_handler.draw(self.screen)
            self.bullet_handler.draw(self.screen)
            self.power_handler.draw(self.screen)
            self.draw_score()
            self.draw_power_time()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def get_score(self):
        self.score = self.enemy_handler.number_enemy_destroyec
        if(self.score > self.max_score):
            self.max_score = self.score

    def draw_menu(self):
        if self.number_death == 0:
            text, text_rect = text_utils.get_message('Press any key to start', 30 ,WHITE_COLOR)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('Press any key to start', SIZE_TITLE ,WHITE_COLOR )
            score, score_rect = text_utils.get_message(TEXT_SHOW_SCORE.format(self.score), SIZE_NORMAL_TEXT , WHITE_COLOR,SCREEN_WIDTH//2,  SCREEN_HEIGHT//2 + 40 )
            maxscore, maxscore_rect = text_utils.get_message(TEXT_SHOW_MAXSCORE.format(self.max_score), SIZE_NORMAL_TEXT , WHITE_COLOR,SCREEN_WIDTH//2,  SCREEN_HEIGHT//2 + 65 )
            number_death, number_death_rect = text_utils.get_message(TEXT_SHOW_DEATH.format(self.number_death), SIZE_NORMAL_TEXT , WHITE_COLOR,SCREEN_WIDTH//2,  SCREEN_HEIGHT//2 + 90)
            self.screen.blit(text, text_rect)
            self.screen.blit(number_death, number_death_rect)
            self.screen.blit(score, score_rect)
            self.screen.blit(maxscore, maxscore_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(TEXT_SHOW_SCORE.format(self.score), SIZE_NORMAL_TEXT ,WHITE_COLOR, SCREEN_WIDTH - 100 ,  20 )
        self.screen.blit(score, score_rect)
    
    def draw_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time - pygame.time.get_ticks())/1000, 2)
            if power_time>=0:
                text, text_rect = text_utils.get_message(f'{self.player.power_type.capitalize()} is enable for {power_time}', 20 ,WHITE_COLOR, 150, 50)
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power = False
                self.player.power_time = DEFAULT_TYPE
                self.player.set_default_image()

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.power_handler.reset()
        self.game_speed = 10
        self.score = 0
        self.contador = 0
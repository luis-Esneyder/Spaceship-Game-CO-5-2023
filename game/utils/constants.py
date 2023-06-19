import pygame
import os
# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
pygame.mixer.init()
MUSIC_START= pygame.mixer.Sound(os.path.join(IMG_DIR, "Music/musicstart.mp3"))
SHOOT_PLAYER= pygame.mixer.Sound(os.path.join(IMG_DIR, "Music/shoot_player.mp3"))
SHOOT_ENEMY= pygame.mixer.Sound(os.path.join(IMG_DIR, "Music/shoot_enemy.mp3"))
ABSOR_HEAR = pygame.mixer.Sound(os.path.join(IMG_DIR, "Music/powerUp2.ogg"))
ABSOR_SHIELD = pygame.mixer.Sound(os.path.join(IMG_DIR, "Music/absor_heart.mp3"))
SHIP_DESTROYEC = pygame.mixer.Sound(os.path.join(IMG_DIR, "Music/splotion.mp3"))
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
BG_START = pygame.image.load(os.path.join(IMG_DIR, 'Other/bg_start.jpg'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
SHIP_RED = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
SHIP_GRAY = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
SHIP_BLACK = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
MALEVOLO_CUCARACHON = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))


FONT_STYLE = 'freesansbold.ttf'

BULLET_ENEMY_TYPE = 'enemy'
BULLET_PLAYER_TYPE = 'player'

WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)
TEXT_COLOR = (152, 152 ,152)
SIZE_TITLE = 30
SIZE_NORMAL_TEXT = 20
TEXT_SHOW_SCORE = 'Your score is: {}'
TEXT_SHOW_MAXSCORE = 'Your score top is: {}'
TEXT_SHOW_DEATH = 'Your death number is : {}'


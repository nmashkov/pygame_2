import uuid
import pathlib

import pygame


# main game settings
NAME = 'Игра 2'
WIDTH, HEIGHT = 700, 900
FPS = 60
bg_color = (239, 239, 239)

# log folder settings
BASE_DIR = str(pathlib.Path().resolve())
BASE_LOGS_DIR = 'logs'
SESSION_DIR = str(uuid.uuid1())

# EVENTS
START_MENU = pygame.USEREVENT + 1
START_TRAIN = pygame.USEREVENT + 2
PRE_EXAM = pygame.USEREVENT + 3
START_EXAM = pygame.USEREVENT + 4
STOP_STAGE = pygame.USEREVENT + 5
RESULT = pygame.USEREVENT + 6
PLAYER_POS = pygame.USEREVENT + 7
WIND = pygame.USEREVENT + 8
UNFREEZE = pygame.USEREVENT + 9

# colors
accent = (41, 166, 236)
back1 = (51, 128, 243)
back1_hover = (27, 87, 177)
back2 = (184, 209, 246)
dark_grey = (51, 51, 51, 100)
light_grey = (170, 170, 170, 100)
light_grey2 = (215, 215, 215, 100)
accent2 = (88, 165, 27)

# player ball settings
player_position = (WIDTH // 2, HEIGHT // 2 + 70)
player_radius = 30
player_mass = 10
player_color = (219, 59, 59, 100)
player_friction = 0.5
player_force = 5000
PLPOSLOG_TIMER = 100
UNFREEZE_TIMER = 600

# player controls
LEFT_1 = pygame.K_a
RIGHT_1 = pygame.K_d
START_1 = pygame.K_w
LEFT_2 = pygame.K_LEFT
RIGHT_2 = pygame.K_RIGHT
START_2 = pygame.K_UP
EXIT = pygame.K_9
CONTINUE = pygame.K_RETURN
DEBUG = pygame.K_8

# earth settings
earth_radius = WIDTH // 2
earth_friction = 0.5

# boundaries settings
boundaries_w = WIDTH
boundaries_h = HEIGHT

# wind settings
wind_timer = 3000
wind_strength = 4000

# warmup settings
warmup_time = 3

# train player and stats settings
health = 3
game_timer = 1

# train difficulty steps
wt_start = 2000
wt_end = 4000
wt_zero = 1500

# exam player and stats settings
exam_health = 3
exam_game_timer = 1

# exam difficulty steps
ex_wt_start = 1000
ex_wt_end = 4000
ex_wt_zero = 1000

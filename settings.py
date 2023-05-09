import uuid
import pathlib

import pygame


# main game settings
NAME = 'Игра 2'
WIDTH, HEIGHT = 700, 900
FPS = 60
bg_color = (190, 190, 190)

# log folder settings
BASE_DIR = str(pathlib.Path().resolve())
BASE_LOGS_DIR = 'logs'
SESSION_DIR = str(uuid.uuid1())

# player ball settings
player_radius = 30
player_mass = 10
player_color = (255, 0, 0, 100)
player_friction = 0.5
player_force = 10000
PLPOSLOG_TIMER = 100

# player controls
LEFT_1 = pygame.K_a
RIGHT_1 = pygame.K_d
START_1 = pygame.K_w
LEFT_2 = pygame.K_LEFT
RIGHT_2 = pygame.K_RIGHT
START_2 = pygame.K_UP
EXIT = pygame.K_ESCAPE
CONTINUE = pygame.K_RETURN

# earth settings
earth_radius = WIDTH // 2
earth_friction = 0.5

# boundaries settings
boundaries_w = WIDTH
boundaries_h = HEIGHT

# wind settings
wind_timer = 3000
wind_strength = 5000

# warmup settings
warmup_time = 1

# train player and stats settings
health = 3

# train difficulty step values

# exam player and stats settings
exam_health = 3

# exam difficulty step values

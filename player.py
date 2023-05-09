import pygame
import pymunk
import pymunk.pygame_util
from datetime import datetime as dt

import settings
import variables
from logger import setup_logger


log_file = 'player.json'
player_log = setup_logger('player_logger', log_file)

log_file = 'player_pos.json'
player_pos_log = setup_logger('player_pos_logger', log_file)


class Player:
    def __init__(self, app):
        self.app = app
        # ball params
        self.player_radius = settings.player_radius
        self.body = pymunk.Body()
        self.body.position = (settings.WIDTH // 2, settings.HEIGHT // 2)
        self.shape = pymunk.Circle(self.body, self.player_radius)
        self.mass = settings.player_mass
        self.shape.color = settings.player_color
        self.shape.friction = settings.player_friction
        # controls
        self.left_button_1 = settings.LEFT_1
        self.right_button_1 = settings.RIGHT_1
        self.left_button_2 = settings.LEFT_2
        self.right_button_2 = settings.RIGHT_2
        self.exit_button = settings.EXIT
        # vars
        self.health = settings.health

    def create_player(self):
        body = self.body
        body.position = self.body.position
        shape = self.shape
        shape.mass = self.mass
        shape.color = self.shape.color
        shape.friction = self.shape.friction
        self.app.space.add(self.body, self.shape)
        return body, shape

    def log_player_pos(self):
        if variables.pl_pos_log:
            player_pos_log.info(
                {
                    'time': f'{dt.now()}',
                    'player_pos': f'{self.body.position.x:.1f}'
                }
            )
            variables.pl_pos_log = False

    def change_state(self):
        # SESSION STATE CHANGE
        if variables.SESSION_STAGE == 'START_TRAIN':
            variables.SESSION_STAGE = 'STOP_STAGE'
            pygame.event.post(
                pygame.event.Event(settings.STOP_STAGE))
            variables.SESSION_STAGE = 'PRE_EXAM'
            pygame.event.post(
                pygame.event.Event(settings.PRE_EXAM))
            self.health = settings.exam_health
        elif variables.SESSION_STAGE == 'START_EXAM':
            variables.SESSION_STAGE = 'STOP_STAGE'
            pygame.event.post(
                pygame.event.Event(settings.STOP_STAGE))
            variables.SESSION_STAGE = 'RESULT'

    def update(self, minutes=settings.game_timer):
        # player chech timer
        if variables.SESSION_STAGE not in ('START_MENU',
                                           'PRE_EXAM',
                                           'STOP_STAGE',
                                           'RESULT'):
            if minutes == settings.game_timer:
                player_log.info(
                    {
                        'time': str(dt.now()),
                        'message': 'time_out',
                        'health': self.health,
                        'player_pos': f'{self.body.position.x:.1f}'
                    }
                )
                self.change_state()
                self.body.position = (settings.WIDTH // 2,
                                      settings.HEIGHT // 2)
            # playet check death
            if self.body.position.x < 50 or self.body.position.x > 650:
                if self.health > 1:
                    self.health -= 1
                    variables.health -= 1
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'death',
                            'health': self.health,
                            'player_pos': f'{self.body.position.x:.1f}'
                        }
                    )
                    self.body.position = (settings.WIDTH // 2,
                                          settings.HEIGHT // 2)
                    self.body.force = (0, 0)
                    variables.wind_direction = 0
                    variables.wind_direction_prev = 0
                else:
                    self.health -= 1
                    variables.health -= 1
                    player_log.info(
                        {
                            'time': str(dt.now()),
                            'message': 'game_over',
                            'health': self.health,
                            'player_pos': f'{self.body.position.x:.1f}'
                        }
                    )
                    self.change_state()
                    self.body.position = (settings.WIDTH // 2,
                                          settings.HEIGHT // 2)
        # player controls
        key = pygame.key.get_pressed()
        if variables.SESSION_STAGE not in ('START_MENU',
                                           'PRE_EXAM',
                                           'STOP_STAGE',
                                           'RESULT'):
            # move left
            # LP
            if key[self.left_button_1]:
                self.body.force -= ((settings.player_force, 0))
            # RP
            if key[self.left_button_2]:
                self.body.force -= ((settings.player_force, 0))
            # move right
            # LP
            if key[self.right_button_1]:
                self.body.force += ((settings.player_force, 0))
            # RP
            if key[self.right_button_2]:
                self.body.force += ((settings.player_force, 0))

        # exit app
        if key[self.exit_button]:
            pygame.event.post(self.app.quit_event)

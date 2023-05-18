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
        self.body.position = settings.player_position
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

    def update(self):
        # player check timer
        if variables.SESSION_STAGE in ('START_TRAIN', 'START_EXAM'):
            if variables.SESSION_STAGE == 'START_TRAIN':
                end_timer = settings.game_timer
            else:
                end_timer = settings.exam_game_timer
            if (variables.minutes >= end_timer and
                    variables.ticks_current > 100):
                player_log.info(
                    {
                        'time': str(dt.now()),
                        'message': 'time_out',
                        'health': self.health,
                        'player_pos': f'{self.body.position.x:.1f}'
                    }
                )
                self.change_state()
                self.body.position = settings.player_position
                self.body.force = (0, 0)
                self.body.angular_velocity = 0
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
                    self.body.position = settings.player_position
                    self.body.force = (0, 0)
                    self.body.angular_velocity = 0
                    variables.wind_direction = 0
                    variables.wind_direction_prev = 0
                    variables.wind_timer = 3000
                    pygame.time.set_timer(settings.WIND, 0)
                    pygame.time.set_timer(settings.WIND, settings.wind_timer)
                    variables.ad_freezed = True
                    pygame.time.set_timer(settings.UNFREEZE,
                                          settings.UNFREEZE_TIMER)
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
                    self.body.position = settings.player_position
                    self.body.force = (0, 0)
                    self.body.angular_velocity = 0
        # player controls
        key = pygame.key.get_pressed()
        if (variables.SESSION_STAGE in ('START_TRAIN', 'START_EXAM') and
                not variables.ad_freezed):
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

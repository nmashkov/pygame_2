"""
Game 2.
Author: Alexey Malishevsky
Programmer: Nikita Mashkov
Designer: Evgeny Manuylenko
Github: https://github.com/nmashkov
2023
"""
import pygame
import pymunk
import pymunk.pygame_util
from datetime import datetime as dt

import settings
import variables
from player import Player
from earth import Earth
from boundaries import Boundaries
from event_manager import event_handler
from fonts import base2
import ui
from debug import debug


class App:
    def __init__(self):
        pygame.init()
        self.res = self.width, self.height = (settings.WIDTH,
                                              settings.HEIGHT)
        self.screen = pygame.display.set_mode(self.res)
        self.clock = pygame.time.Clock()
        self.fps = settings.FPS
        self.app_name = settings.NAME
        self.bg_color = settings.bg_color
        self.pygame_icon = pygame.image.load('media/icon.ico')
        self.quit_event = pygame.event.Event(pygame.QUIT)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        self.player = Player(self)
        self.earth = Earth(self)
        self.boundaries = Boundaries(self)

    def app_caption(self, mode='menu'):
        current_fps = self.clock.get_fps()
        if mode == 'game':
            pygame.display.set_caption(f'{self.app_name}. '
                                       f'Попытки: {self.player.health}. '
                                       f'FPS: {current_fps:.2f}')
        if mode == 'menu':
            pygame.display.set_caption(f'{self.app_name}. '
                                       f'FPS: {current_fps:.2f}')

    def debug_panel(self, player_body=0):
        debug(variables.SESSION_STAGE, 'SESSION_STAGE')
        debug(variables.health, 'health', 70)
        debug(variables.wind_direction, 'wind_direction', 90)
        debug(variables.wind_direction_prev, 'wind_direction_prev', 110)
        debug(variables.wind_timer, 'wind_timer', 130)
        debug(variables.lp_active_time, 'lp_active_time', 150)
        debug(variables.lp_key_pushes, 'lp_key_pushes', 170)
        debug(variables.rp_active_time, 'rp_active_time', 190)
        debug(variables.rp_key_pushes, 'rp_key_pushes', 210)
        debug(variables.conflict, 'conflict', 230)
        debug(variables.conflict_time, 'conflict_time', 250)
        debug(variables.cooperation, 'cooperation', 270)
        debug(variables.cooperative_time, 'cooperative_time', 290)
        if player_body:
            debug(player_body.force, 'player_body.force', 310)

    def update(self, player_body, minutes):
        # wind
        player_body.force += (variables.wind_direction *
                              settings.wind_strength, 0)
        # player
        self.player.update(minutes)
        if variables.debug_activated:
            self.debug_panel(player_body)

    def draw(self, minutes, seconds):
        self.space.debug_draw(self.draw_options)
        ui.ui_game(self.screen, minutes, seconds)
        pygame.display.update()

    def start_menu(self):
        pygame.event.post(pygame.event.Event(settings.START_MENU))
        variables.SESSION_STAGE = 'START_MENU'

        in_menu = True
        while in_menu:
            self.clock.tick(15)

            pygame.display.set_icon(self.pygame_icon)

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update()

            key = pygame.key.get_pressed()
            if key[settings.START_1] and key[settings.START_2]:
                pygame.event.post(pygame.event.Event(settings.START_TRAIN))
                variables.SESSION_STAGE = 'START_TRAIN'
                in_menu = False

            ui.ui_menu(self.screen)

            pygame.display.update()

            self.app_caption('menu')

    def warmup(self):
        start_ticks = pygame.time.get_ticks()
        while True:
            self.screen.fill(self.bg_color)

            self.space.debug_draw(self.draw_options)
            ui.ui_game(self.screen, 0, 0)

            seconds = (settings.warmup_time -
                       (pygame.time.get_ticks() - start_ticks) * 0.001)

            draw_sec = base2.render(f'{seconds:.2f}', True, settings.dark_grey)
            draw_sec_width = draw_sec.get_width()
            self.screen.blit(draw_sec,
                             (settings.WIDTH // 2 - draw_sec_width * .5,
                              settings.HEIGHT // 2 - 40))

            if seconds <= 0.03:
                break

            pygame.display.update()

            self.clock.tick(30)

        variables.is_warmuped = True
        # reset timers
        variables.ticks = pygame.time.get_ticks()
        variables.start_stage_time = dt.now()
        # start pl pos logs
        variables.pl_pos_log = True
        pygame.time.set_timer(settings.PLAYER_POS, settings.PLPOSLOG_TIMER)
        # start wind
        variables.wind_direction = 0
        variables.wind_direction_prev = 0
        pygame.time.set_timer(settings.WIND, settings.wind_timer)

    def game(self, player_body, minutes, seconds):

        self.screen.fill(self.bg_color)

        if not variables.is_warmuped:
            self.warmup()

        self.update(player_body, minutes)
        self.draw(minutes, seconds)

        self.app_caption('game')

    def pre_exam(self):

        in_pre_exam = True
        while in_pre_exam:
            self.clock.tick(15)

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update()

            key = pygame.key.get_pressed()
            if key[settings.START_1] and key[settings.START_2]:
                pygame.event.post(pygame.event.Event(settings.START_EXAM))
                variables.SESSION_STAGE = 'START_EXAM'
                in_pre_exam = False

            ui.ui_pre_exam(self.screen)

            if variables.debug_activated:
                self.debug_panel()

            pygame.display.update()

            self.app_caption()

    def result(self):
        pygame.event.post(pygame.event.Event(settings.RESULT))

        in_result = True
        while in_result:
            self.clock.tick(15)

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update()

            key = pygame.key.get_pressed()
            if key[settings.EXIT] or key[settings.CONTINUE]:
                in_result = False

            ui.ui_result(self.screen)

            if variables.debug_activated:
                self.debug_panel()

            pygame.display.update()

            self.app_caption()

        pygame.event.post(self.quit_event)
        event_handler()

    def run(self):

        self.start_menu()

        player_body, player_shape = self.player.create_player()

        delta_t = 1 / self.fps

        while True:
            # delta_t = self.clock.tick(self.fps) * 0.001 * 60

            ticks = pygame.time.get_ticks() - variables.ticks
            seconds = int(ticks / 1000 % 60)
            minutes = int(ticks / 60000 % 24)

            event_handler()

            if variables.SESSION_STAGE == 'RESULT':
                break

            elif variables.SESSION_STAGE == 'START_EXAM':
                self.game(player_body, minutes, seconds)
                self.player.log_player_pos()

            elif variables.SESSION_STAGE == 'PRE_EXAM':
                self.pre_exam()

            elif variables.SESSION_STAGE == 'START_TRAIN':
                self.game(player_body, minutes, seconds)
                self.player.log_player_pos()

            self.space.step(delta_t)
            self.clock.tick(self.fps)

        self.result()


if __name__ == '__main__':
    app = App()
    app.run()

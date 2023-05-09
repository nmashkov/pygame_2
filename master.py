"""
Game 2.
Author: Nikita Mashkov
Github: https://github.com/nmashkov
2023
"""
import pygame
import pymunk
import pymunk.pygame_util

import settings
import variables
from player import Player
from earth import Earth
from boundaries import Boundaries
from event_manager import event_handler
import ui


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
        self.font = pygame.font.Font(None, 30)
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
                                       f'Health: {self.player.health}. '
                                       f'FPS: {current_fps:.2f}')
        if mode == 'menu':
            pygame.display.set_caption(f'{self.app_name}. '
                                       f'FPS: {current_fps:.2f}')

    def update(self, player_body):
        # wind
        player_body.force += (variables.wind_direction *
                              settings.wind_strength, 0)
        # player
        self.player.update()

    def draw(self, player_body, minutes, seconds):
        self.space.debug_draw(self.draw_options)
        ui.ui_game(self.screen, self.font, player_body, minutes, seconds)
        pygame.display.flip()

    def start_menu(self):
        pygame.event.post(pygame.event.Event(settings.START_MENU))
        variables.SESSION_STAGE = 'START_MENU'

        in_menu = True
        while in_menu:
            self.clock.tick(15)

            event_handler()

            self.screen.fill(self.bg_color)

            self.player.update()

            key = pygame.key.get_pressed()
            if key[settings.START_1] and key[settings.START_2]:
                pygame.event.post(pygame.event.Event(settings.START_TRAIN))
                pygame.time.set_timer(settings.WIND, settings.wind_timer)
                variables.SESSION_STAGE = 'START_TRAIN'
                in_menu = False

            ui.ui_menu(self.screen, self.font)

            pygame.display.update()

            self.app_caption('menu')

    def warmup(self):
        start_ticks = pygame.time.get_ticks()
        while True:
            self.screen.fill(self.bg_color)

            seconds = (pygame.time.get_ticks() - start_ticks) / 1000

            self.screen.blit(
                self.font.render(f'{seconds:.2f}', True, 'black'),
                (settings.WIDTH // 2 - 30, settings.HEIGHT // 2))

            if seconds > settings.warmup_time:
                break

            pygame.display.update()

            self.clock.tick(30)

        variables.is_warmuped = True

    def train(self, player_body, minutes, seconds):

        self.screen.fill(self.bg_color)

        if not variables.is_warmuped:
            self.warmup()

        self.update(player_body)
        self.draw(player_body, minutes, seconds)

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
                pygame.time.set_timer(settings.WIND, settings.wind_timer)
                in_pre_exam = False

            ui.ui_pre_exam(self.screen, self.font)

            pygame.display.update()

            self.app_caption(mode='game')

    def exam(self, player_body, minutes, seconds):

        self.screen.fill(self.bg_color)

        if not variables.is_warmuped:
            self.warmup()

        self.update(player_body)
        self.draw(player_body, minutes, seconds)

        self.app_caption('game')

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

            ui.ui_result(self.screen, self.font)

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

            ticks = pygame.time.get_ticks()
            seconds = int(ticks/1000 % 60)
            minutes = int(ticks/60000 % 24)

            event_handler()

            if variables.SESSION_STAGE == 'START_TRAIN':
                self.train(player_body, minutes, seconds)
                self.player.log_player_pos()

            if variables.SESSION_STAGE == 'START_EXAM':
                self.exam(player_body, minutes, seconds)
                self.player.log_player_pos()

            if variables.SESSION_STAGE == 'PRE_EXAM':
                self.pre_exam()

            if variables.SESSION_STAGE == 'RESULT':
                break

            self.space.step(delta_t)
            self.clock.tick(self.fps)

        self.result()


if __name__ == '__main__':
    app = App()
    app.run()

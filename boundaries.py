# import pygame
import pymunk
import pymunk.pygame_util

import settings


class Boundaries:
    def __init__(self, app):
        self.app = app
        self.player = self.app.player
        # boundaries params
        self.bounds_w = settings.boundaries_w
        self.bounds_h = settings.boundaries_h
        self.rects = [
            [(self.bounds_w*.5, self.bounds_h - 10), (self.bounds_w, 20)],
            [(self.bounds_w*.5, 10), (self.bounds_w, 20)],
            [(10, self.bounds_h*.5), (20, self.bounds_h)],
            [(self.bounds_w - 10, self.bounds_h*.5), (20, self.bounds_h)],
        ]
        for pos, size in self.rects:
            self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.body.position = pos
            self.shape = pymunk.Poly.create_box(self.body, size)
            self.app.space.add(self.body, self.shape)

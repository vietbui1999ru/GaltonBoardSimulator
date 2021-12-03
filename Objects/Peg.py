import pymunk as pm, pygame as pg
from pymunk import pygame_util

pm.pygame_util.positive_y_is_up = False

COLOR = 'darkslateblue'
RADIUS = 10


class Peg:
    def __init__(self, x=0, y=0, color=COLOR, radius=RADIUS):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def create_peg(self, x, y, space):
        circle_shape = pm.Circle(space.static_body, radius=self.radius, offset=(x, y))
        circle_shape.color = pg.color.THECOLORS[self.color]
        circle_shape.elasticity = 0.1
        circle_shape.friction = 0.5
        space.add(circle_shape)

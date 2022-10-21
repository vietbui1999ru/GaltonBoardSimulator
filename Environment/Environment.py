import matplotlib
import matplotlib.pyplot as plt
import pygame as pg
import pymunk as pm
import pymunk.pygame_util
from random import randrange

matplotlib.use('Agg')
import matplotlib.backends.backend_agg as agg

from Game_Menu.Simulation_menu import Menu
from Objects.Ball import Ball
from Objects.Peg import Peg
from Objects.Segment import Segment
from Environment.Probability import Prob
from Game_Menu.Settings import Settings

pm.pygame_util.positive_y_is_up = False

NUM_BALLS = Settings().num_balls
WIDTH, HEIGHT = Menu().get_width_height()

a, b, c, d = 40, 100, 18, 40
x1, x2, x3, x4 = a, WIDTH // 2 - c - 11, WIDTH // 2 + c - 11, WIDTH - a
y1, y2, y3, y4, y5 = b, HEIGHT // 4 - d, HEIGHT // 4, HEIGHT // 2 - 1.5 * b, HEIGHT - 4 * b
L1, L2, L3, L4 = (x1, -100), (x1, y1), (x2, y2), (x2, y3)
R1, R2, R3, R4 = (x4, -100), (x4, y1), (x3, y2), (x3, y3)
B1, B2 = (0, HEIGHT), (WIDTH, HEIGHT)
# H = 800
# W = 800
G = 9810
FPS = 60


def set_timer():
    return pg.time.Clock()


def create_surface(w, h):
    surface = pg.display.set_mode((w, h))
    return surface


class Environment:
    # Create the Environment of Galton Board
    def __init__(self, w=WIDTH, h=HEIGHT, g=G, fps=FPS):
        self.h = h
        self.w = w
        self.g = g
        self.fps = fps

        space = pm.Space()
        space.gravity = 0, self.g
        self.space = space

    # create surface of environment

    # set timer for the environment

    # set gravity
    # def create_gravity(self, g):
    #     space = pm.Space()
    #     space.gravity = 0, g
    #     return space

    # Draw
    def draw_options(self):
        surface = create_surface(self.w, self.h)
        return pm.pygame_util.DrawOptions(surface)

    # Create pegs
    def draw_pegs(self, peg_y=y4, step=60):
        for i in range(10):
            peg_x = -1.5 * step if i % 2 else -step
            for j in range(self.w // step + 2):
                Peg().create_peg(peg_x, peg_y, self.space)
                if i == 9:
                    Segment().create_seg((peg_x, peg_y + 50), (peg_x, self.h), self.space)
                peg_x += step
            peg_y += 0.5 * step

    # create platform
    def create_platform(self):
        platforms = (L1, L2), (L2, L3), (L3, L4), (R1, R2), (R2, R3), (R3, R4)
        for platform in platforms:
            Segment().create_seg(*platform, self.space)
        Segment().create_seg(B1, B2, self.space)

    # Create falling balls
    def draw_balls(self, num_balls):
        balls = [([randrange(256) for i in range(3)], Ball().create_ball(self.space, x1, x4, y1)) for j in
                 range(num_balls)]
        return balls

    # Create funnel
    def draw_segment(self):
        pass

    # Customize gravity
    def set_gravity(self, g):
        self.space.gravity = 0, g

    # Customize resolution
    def set_resolution(self, W, H):
        pass

    # start game

    def start_g(self):
        surface = create_surface(self.w, self.h)
        self.draw_pegs()
        self.create_platform()
        balls = self.draw_balls(NUM_BALLS)
        while True:
            surface.fill(pg.Color('black'))

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()

            self.space.step(1 / self.fps)
            draw_options = self.draw_options()
            self.space.debug_draw(draw_options)
            [pg.draw.circle(surface, color, (int(ball.position[0]), int(ball.position[1])),
                            Ball().get_radius()) for color, ball in balls]

            pg.display.flip()
            clock = set_timer()
            clock.tick(self.fps)

    def start_p(self):
        fig = plt.figure(figsize=(5, 5))
        # plt.scatter(Prob().bell_curve()[0], Prob().bell_curve()[1], marker='o', s=25, color='red')
        plt.bar(range(Prob().get_lines() + 1), Prob().start_p())
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        screen = create_surface(self.w, self.h)

        size = canvas.get_width_height()
        surf = pg.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, (100, 100))
        pg.display.flip()
        show = True
        while show:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    # Stop showing when quit
                    show = False
            pg.display.update()

    # Customize num pegs

    # Customize num falling balls
    # Customize num static balls
    # Customize color of environment

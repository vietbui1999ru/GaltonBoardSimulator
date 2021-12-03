import sys

import pymunk as pm
import pygame as pg
import pygame_gui as ui
from Objects.InputBox import InpBox

def set_timer():
    return pg.time.Clock()

def create_surface(w, h):
    surface = pg.display.set_mode((w, h))
    return surface
class Settings:

    def __init__(self, res=(800, 800), color=(255, 255, 255),
                 color_light=(170, 170, 170),
                 color_dark=(100, 100, 100)):
        self.res = res
        self.color = color
        self.color_light = color_light
        self.color_dark = color_dark
        self.num_balls = 600
        self.funnel_width = 18

    def input_(self, text):
        pass
    def start(self):
        surface = create_surface(self.res[0], self.res[1])
        clock = set_timer()
        # text_b1 =
        input_b1 = InpBox(100, 100, 140, 32, 'Number of balls')
        input_b2 = InpBox(100, 300, 140, 32, 'Funnel Width')
        inp_boxes = [input_b1, input_b2]

        while True:
            surface.fill(pg.Color('turquoise'))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    show = False
                    pg.quit()
                for box in inp_boxes:
                    box.handle_event(event)
                    value = box.get_input(box.text)
                    if value is not None:
                        self.num_balls = value
                        pg.quit()
                        from Environment.Environment import Environment
                        Environment().start_g()

            for box in inp_boxes:
                box.update()

            surface.fill((30, 30, 30))
            for box in inp_boxes:
                box.draw(surface)

            pg.display.flip()
            clock.tick(30)


import pygame
import pygame as pg
import pymunk as pm
import sys
import random


class Menu:
    def __init__(self, res=(800, 800), color=(255, 255, 255),
                 color_light=(170, 170, 170),
                 color_dark=(100, 100, 100)):

        self.res = res
        self.color = color
        self.color_light = color_light
        self.color_dark = color_dark

    def create_window(self, res):
        return pg.display.set_mode(res)

    def get_width_height(self):
        screen = self.create_window(self.res)
        return screen.get_width(), screen.get_height()

    def define_font(self, font='Corbel', size=35):
        return pygame.font.SysFont(font, size)

    def get_color(self):
        return self.color

    def get_color_light(self):
        return self.color_light

    def get_color_dark(self):
        return self.color_dark


    def button(self, screen, text, x1, x2, y1, y2, text_pos_x, text_pos_y):
        mouse = pg.mouse.get_pos()
        width = self.res[0]
        height = self.res[1]
        thiccness = abs(y2 - y1)
        widthness = abs(x2 - x1)
        if width / 2 + x1 <= mouse[0] <= width / 2 + x2 and height / 2 + y1 <= mouse[1] <= height / 2 + y2:
            pg.draw.rect(screen, color=self.get_color_light(),
                         rect=[width / 2 + x1, height / 2 + y1, widthness, thiccness])
        else:
            pg.draw.rect(screen, color=self.get_color_dark(),
                         rect=[width / 2 + x1, height / 2 + y1, widthness, thiccness])
        screen.blit(text, (width / 2 + text_pos_x, height / 2 + text_pos_y))

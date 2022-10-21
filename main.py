import sys

import pygame as pg
import pygame_gui as ui
from Environment.Environment import Environment
from Game_Menu.Simulation_menu import Menu
from Game_Menu.Settings import Settings

# This is text input
WIDTH = 800
HEIGHT = 800

# size settings
x1 = -40
x2 = 100
start_y1_g = -140
start_y2_g = -100
start_y1_p = -80
start_y2_p = -40
settings_y1 = -20
settings_y2 = 20
exit_y1 = 40
exit_y2 = 80
start_str_g = 'Physics'
start_str_p = 'Probability'
settings_str = 'Settings'
exit_str = 'Exit'

pg.init()

menu = Menu((WIDTH, HEIGHT))
width, height = menu.get_width_height()
screen = menu.create_window(res=(width, height))
text = menu.define_font()

start_g = text.render(start_str_g, True, menu.get_color())
start_p = text.render(start_str_p, True, menu.get_color())
settings = text.render(settings_str, True, menu.get_color())
quit_game = text.render(exit_str, True, menu.get_color())

while True:
    mouse = pg.mouse.get_pos()
    for ev in pg.event.get():

        if ev.type == pg.QUIT:
            pg.quit()

        # check if mouse is clicked
        if ev.type == pg.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the button
            if width / 2 + x1 <= mouse[0] <= width / 2 + x2 and height / 2 + start_y1_g <= mouse[
                1] <= height / 2 + start_y2_g:
                pg.quit()
                Environment(WIDTH, HEIGHT).start_g()
            # the simulation will start
            if width / 2 + x1 <= mouse[0] <= width / 2 + x2 and height / 2 + start_y1_p <= mouse[
                1] <= height / 2 + start_y2_p:
                pg.quit()
                Environment(WIDTH, HEIGHT).start_p()

            # if the mouse is clicked on the button
            # directs to settings of the game
            elif width / 2 + x1 <= mouse[0] <= width / 2 + x2 and height / 2 + settings_y1 <= mouse[
                1] <= height / 2 + settings_y2:
                pg.quit()
                Settings().start()

            # if the mouse is clicked on the button
            # the simulation is terminated
            if width / 2 + x1 <= mouse[0] <= width / 2 + x2 and height / 2 + exit_y1 <= mouse[
                1] <= height / 2 + exit_y2:
                pg.quit()
                # pdb.set_trace()
                sys.exit(0)

    # fill screen with color
    screen.fill((60, 25, 60))

    # store (x,y) coordinates into
    # variable as a tuple

    # if mouse is hovered on a button
    # it changes to lighter shade

    menu.button(screen, start_p, x1, x2, start_y1_p, start_y2_p, -40, start_y1_p)
    menu.button(screen, start_g, x1, x2, start_y1_g, start_y2_g, -20, start_y1_g)
    menu.button(screen, settings, x1, x2, settings_y1, settings_y2, -25, settings_y1)
    menu.button(screen, quit_game, x1, x2, exit_y1, exit_y2, 5, exit_y1)

    # update frames of game
    pg.display.update()

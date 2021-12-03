import pymunk as pm
import pymunk.pygame_util

pm.pygame_util.positive_y_is_up = False
from random import randrange
from Game_Menu.Simulation_menu import Menu

WIDTH, HEIGHT = Menu().get_width_height()

# a, b, c, d = 100, 100, 18, 40
# x1, x2, x3, x4 = a, WIDTH // 2 - c, WIDTH // 2 + c, WIDTH - a
# y1, y2, y3, y4, y5 = b, HEIGHT // 4 - d, HEIGHT // 4, HEIGHT // 2 - 1.5 * b, HEIGHT - 4 * b

BALL_MASS, BALL_RADIUS = 1, 7


class Ball:
    def __init__(self, mass=BALL_MASS, radius=BALL_RADIUS):
        self.mass = mass
        self.radius = radius

    def create_ball(self, space, x1, x4, y1):
        ball_moment = pm.moment_for_circle(self.mass, 0, self.radius)
        ball_body = pm.Body(self.mass, ball_moment)
        ball_body.position = randrange(x1, x4), randrange(-y1, y1)
        ball_shape = pm.Circle(ball_body, self.radius)
        ball_shape.elasticity = 0.1
        ball_shape.friction = 0.1
        space.add(ball_body, ball_shape)
        return ball_body

    def get_radius(self):
        return self.radius

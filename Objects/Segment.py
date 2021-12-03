import pygame as pg
import pymunk as pm
import pymunk.pygame_util

pm.pygame_util.positive_y_is_up = False

SEG_THICKNESS = 6
COLOR = 'darkolivegreen'


class Segment:
    def __init__(self, seg_thickness=SEG_THICKNESS, color=COLOR):
        self.seg_thickness = seg_thickness
        self.color = color

    def create_seg(self, from_, to_, space):
        segment_shape = pm.Segment(space.static_body, from_, to_, self.seg_thickness)
        segment_shape.color = pg.color.THECOLORS[self.color]
        space.add(segment_shape)

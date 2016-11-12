from pygame.rect import Rect
from settings import *
import pygame
import math

class Walls:
    def __init__(self):
        ''' keep track of the walls
        you could maybe pass in a COLOR here'''
        self.walls = []

    def add_wall(self, x, y, w, h):
        ''' add a single wall'''
        self.walls.append(Rect(x,y,w,h))

    def parse_level(self, level):
        '''Parse a level string into a set of walls. I've made this for you'''
        level_width = len(level[0])
        wall_width = math.ceil(WIDTH / level_width)

        level_height = len(level)
        wall_height = math.ceil(HEIGHT / level_height)
        print("Level Width: {}, Level Height: {}".format(level_width, level_height))
        print("Wall Width: {}, Wall Height: {}".format(wall_width, wall_height))

        for row_index in range(level_height):
            for col_index in range(level_width):
                cell = level[row_index][col_index]

                if cell == "W":
                    x = wall_width * col_index
                    y = wall_height * row_index
                    self.add_wall(x, y, wall_width, wall_height)

    def set_example_level(self):
        level = [
            "WWWWWWWWWWWWW",
            "W      W    W",
            "W  W   W    W",
            "W  W   W    W",
            "W  W        W",
            "WWWWWWWWWWWWW"
        ]
        self.parse_level(level)

    def platform_level(self):
        level = [
            "WWWWWWWWWWWWWWWWWWWWW",
            "W                   W",
            "W    WWWWW    WWWW  W",
            "W WW       WW       W",
            "W     WWW      WWW  W",
            "WWWWWWWWWWWWWWWWWWWWW"
        ]
        self.parse_level(level)

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, BLACK, wall)
            ### fill in the pygame draw code here.
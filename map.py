import pygame as pg
from settings import *

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.world_map = {}
        self.parse_map()

    def parse_map(self):
        """Convert mini map to world coordinates"""
        for j, row in enumerate(self.mini_map):
            for i, cell in enumerate(row):
                if cell:
                    self.world_map[(i, j)] = cell

    def draw(self):
        """Draw minimap"""
        pass
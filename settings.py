from math import cos, sin, radians, sqrt, ceil, pi
from random import uniform, randint
import pygame as pg
import numpy as np

RES = WIDTH, HEIGHT = 800, 600
FPS = 60
TIME_SCALE = 1
DT = TIME_SCALE * 1 / FPS
TERRAIN_POINTS_NUMBER = 50
TERRAIN_GENERATION_X_STEP = .2
TERRAIN_GENERATION_Y_SCALE = 70
TERRAIN_X_INTERVAL = ceil(WIDTH / TERRAIN_POINTS_NUMBER)
PIXEL_PER_METER = 5
LANDER_WIDTH = 5
LANDER_HEIGHT = 5
LANDER_WIDTH_PX = LANDER_WIDTH * PIXEL_PER_METER
LANDER_HEIGHT_PX = LANDER_HEIGHT * PIXEL_PER_METER
FLAT_SURFACE_SIZE = ceil(TERRAIN_POINTS_NUMBER / (WIDTH / LANDER_WIDTH_PX)) + 1
GRAVITY = 1.6 * PIXEL_PER_METER
THRUST_VALUE = 5 * PIXEL_PER_METER
ROTATION_SPEED = 1

BLACK = (10, 10, 10)
WHITE = (240, 240, 240)

import settings
from settings import uniform, randint, pi, sin
from Coordinates import Coordinates


class Terrain:
    def __init__(self):
        self.points = None
        self.flat_surface_index = 0
        self.flat_surface_start = None
        self.flat_surface_end = None
        self.flat_surface_center = None
        self.generate_terrain()

    def generate_terrain(self) -> None:
        self.points = []
        self.flat_surface_index = randint(4, settings.TERRAIN_POINTS_NUMBER - 4)
        f = (lambda x: (sin(2 * x) + sin(pi * x)) * settings.TERRAIN_GENERATION_Y_SCALE + settings.HEIGHT - 150)
        origin_x = uniform(0, 1000)
        i = 0
        while i <= settings.TERRAIN_POINTS_NUMBER:
            if i == self.flat_surface_index + 1:
                self.flat_surface_start = Coordinates((i - 1) * settings.TERRAIN_X_INTERVAL, self.points[-1].y)
                self.flat_surface_end = Coordinates(((i - 1) + settings.FLAT_SURFACE_SIZE) * settings.TERRAIN_X_INTERVAL, self.points[-1].y)
                self.flat_surface_center = Coordinates((self.flat_surface_start.x + self.flat_surface_end.x) / 2, self.points[-1].y)
                for _ in range(0, settings.FLAT_SURFACE_SIZE):
                    self.points.append(Coordinates(i * settings.TERRAIN_X_INTERVAL, self.points[-1].y))
                    i += 1
            else:
                self.points.append(Coordinates(
                    i * settings.TERRAIN_X_INTERVAL,
                    f(origin_x + i * settings.TERRAIN_GENERATION_X_STEP)
                ))
                i += 1

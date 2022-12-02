import settings
from settings import cos, sin, radians, sqrt
from Coordinates import Coordinates
from Terrain import Terrain
from State import State


class Lander:
    """
    Lunar Lander module

    Attributes:
        origin_position:    position of the lander at the instantiation
        position:           current position of the lander
        speed:              speed vector of the lander
        rotation:           rotation of the lander in degrees, the pivot point is the center of the object
        max_fuel:           fuel value at its instantiation
        fuel:               current fuel value
        size:               size of the lander in pixels
        thrust:             True if the reactors are on, False if they are off
        rotation_direction: -1 if it rotates right, 1 if it rotates left, 0 if there is no rotation
        terrain:            terrain of the game
        died:              True if it is still alive, False otherwise
    """
    def __init__(self, max_fuel: int, size: Coordinates, position: Coordinates = Coordinates(0, 0),
                 speed: Coordinates = Coordinates(0, 0), terrain: Terrain = None):
        self.origin_position: Coordinates = position
        self.position: Coordinates = self.origin_position
        self.speed: Coordinates = speed
        self.rotation: float = 0
        self.max_fuel: int = max_fuel
        self.fuel: int = self.max_fuel
        self.size: Coordinates = size.multiply_by_scalar(settings.PIXEL_PER_METER)
        self.thrust: bool = False
        self.rotation_direction: int = 0
        self.terrain: Terrain = terrain
        self.died: bool = False
        self.scored: bool = False
        self.score: int = 0

    def rotate(self, angle: float) -> None:
        self.rotation += angle
        self.rotation = max(self.rotation, -90)
        self.rotation = min(self.rotation, 90)

    def update(self) -> None:
        self.died = False
        self.scored = False
        if self.collides_with_terrain():
            if self.is_on_goal():
                self.scored = True
                self.score += 1
            else:
                self.died = True
                self.score -= 1
            self.terrain.generate_terrain()
            self.reset()
        else:
            self.rotate(settings.ROTATION_SPEED * self.rotation_direction)
            rotation_rad = radians(self.rotation + 90)

            if self.thrust and self.fuel > 0:
                self.fuel -= 1
                thrust_vector = Coordinates(
                    cos(rotation_rad),
                    sin(rotation_rad) * -1  # * -1 because y goes up downwards
                ).multiply_by_scalar(settings.THRUST_VALUE * settings.DT)
                self.speed += thrust_vector

            self.speed += Coordinates(0, settings.GRAVITY * settings.DT)
            self.position += self.speed.multiply_by_scalar(settings.DT)
            self.thrust = 0
            self.rotation_direction = 0

    def collides_with_terrain(self) -> bool:
        for i in range(len(self.terrain.points) - 1):
            point = self.terrain.points[i]
            next_point = self.terrain.points[i + 1]
            if self.position.y + self.size.y < min(point.y, next_point.y):
                continue
            if point.x - self.size.x < self.position.x < next_point.x:
                return True
        return False

    def is_on_goal(self) -> bool:
        if self.collides_with_terrain():
            return self.terrain.flat_surface_start.x < self.position.x < self.terrain.flat_surface_end.x - self.size.x
        return False

    def get_distance_from_goal(self) -> float:
        return sqrt((self.position.x + self.size.x / 2 - self.terrain.flat_surface_center.x) ** 2 + (self.position.y + self.size.y / 2 - self.terrain.flat_surface_center.y) ** 2)

    def get_closest_obstacle(self) -> Coordinates:
        closest_point = Coordinates()
        distance_from_closest_point = 99999
        for i in range(len(self.terrain.points) - 1):
            point = self.terrain.points[i]
            distance = sqrt((self.position.x + self.size.x / 2 - point.x) ** 2 + (self.position.y + self.size.y / 2 - point.y) ** 2)
            if distance < distance_from_closest_point:
                distance_from_closest_point = distance
                closest_point = point
        return closest_point

    def reset(self) -> None:
        self.died = True
        self.position = self.origin_position
        self.speed = Coordinates(0, 0)
        self.rotation = 0
        self.fuel = self.max_fuel
        self.thrust = 0

    def get_state(self) -> State:
        closest_obstacle = self.get_closest_obstacle()
        return State(
            self.position.x,
            self.position.y,
            self.speed.x,
            self.speed.y,
            self.rotation,
            self.get_distance_from_goal(),
            closest_obstacle.x,
            closest_obstacle.y,
            self.died,
            self.scored
        )


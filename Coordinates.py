from __future__ import annotations


class Coordinates:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    def __add__(self, other: Coordinates) -> Coordinates:
        return Coordinates(self.x + other.x, self.y + other.y)

    def multiply_by_scalar(self, scalar: float) -> Coordinates:
        return Coordinates(self.x * scalar, self.y * scalar)

    def round(self) -> Coordinates:
        return Coordinates(round(self.x), round(self.y))

    def to_tuple(self) -> (int, int):
        return self.x, self.y

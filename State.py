class State:
    """
    State of the lander at a given time

    Attributes:
        x:                  x position
        y:                  y position
        x_velocity:         vertical velocity
        y_velocity:         horizontal velocity
        rotation:           rotation in degrees
        distance_from_goal: distance from the center of the goal (flat surface)
        closest_obstacle_x: x position of the closest terrain point
        closest_obstacle_y: y position of the closest terrain point
        crashed:            True if he crashed at during the last action, False otherwise
        scored:             True if he scored at during the last action, False otherwise
    """
    def __init__(self, x: float, y: float, x_velocity: float, y_velocity: float, rotation: float, distance_from_goal: float, closest_obstacle_x: float, closest_obstacle_y: float, crashed: bool, scored: bool):
        self.x: float = x
        self.y: float = y
        self.x_velocity: float = x_velocity
        self.y_velocity: float = y_velocity
        self.rotation: float = rotation
        self.distance_from_goal: float = distance_from_goal
        self.closest_obstacle_x: float = closest_obstacle_x
        self.closest_obstacle_y: float = closest_obstacle_y
        self.crashed: bool = crashed
        self.scored: bool = scored

    def __str__(self) -> str:
        return f"--- State ---\n" \
               f"Position: (x: {round(self.x)}, y: {round(self.y)})\n" \
               f"Speed: (x: {round(self.x_velocity)}, y: {round(self.y_velocity)})\n" \
               f"Rotation: {self.rotation}°\n" \
               f"Distance from goal: {round(self.distance_from_goal)}\n" \
               f"Closest obstacle: (x: {round(self.closest_obstacle_x)}, y: {round(self.closest_obstacle_y)})"

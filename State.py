class State:
    def __init__(self, x: float, y: float, x_velocity: float, y_velocity: float, rotation: float, distance_from_goal: float, closest_obstacle_x: float, closest_obstacle_y: float, died: bool, won: bool):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.rotation = rotation
        self.distance_from_goal = distance_from_goal
        self.closest_obstacle_x = closest_obstacle_x
        self.closest_obstacle_y = closest_obstacle_y
        self.died = died
        self.won = won

    def __str__(self) -> str:
        return f"--- State ---\n" \
               f"Position: (x: {round(self.x)}, y: {round(self.y)})\n" \
               f"Speed: (x: {round(self.x_velocity)}, y: {round(self.y_velocity)})\n" \
               f"Rotation: {self.rotation}°\n" \
               f"Distance from goal: {round(self.distance_from_goal)}\n" \
               f"Closest obstacle: (x: {round(self.closest_obstacle_x)}, y: {round(self.closest_obstacle_y)})"

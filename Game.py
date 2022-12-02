import settings
from settings import pg
from Lander import Lander
from Terrain import Terrain
from Coordinates import Coordinates


class Game:
    """
    GUI of the game

    Attributes:
        screen:         PyGame surface where the game is displayed
        clock:          PyGame clock of the game
        terrain:        terrain of the current game
        lander:         player's lander
        lander_sprite:  sprite of the lander
        font:           PyGame font of the text
    """
    def __init__(self):
        self.screen = pg.display.set_mode(settings.RES)
        self.clock = pg.time.Clock()
        self.terrain = Terrain()
        self.lander = Lander(500, Coordinates(settings.LANDER_WIDTH, settings.LANDER_HEIGHT), position=Coordinates(300, 10), terrain=self.terrain)
        self.lander_sprite = pg.transform.scale(
            pg.image.load("assets/lander.png").convert_alpha(),
            self.lander.size.to_tuple()
        )
        self.font = None

    def draw_game(self) -> None:
        """
        Draws the game (terrain and lander)
        """
        self.screen.fill(settings.BLACK)
        self.draw_terrain()
        self.draw_lander()
        pg.display.update()

    def draw_lander(self) -> None:
        """
        Draws the lander and all its information.
        """
        remaining_fuel = self.font.render("Fuel: " + str(self.lander.fuel), True, settings.WHITE)
        vertical_speed = self.font.render("Vertical Speed: " + str(round(self.lander.speed.y)), True, settings.WHITE)
        horizontal_speed = self.font.render("Horizontal Speed: " + str(round(self.lander.speed.x)), True, settings.WHITE)
        score = self.font.render("Score: " + str(round(self.lander.score)), True, settings.WHITE)
        self.screen.blit(remaining_fuel, (settings.WIDTH - remaining_fuel.get_width() - 10, 10))
        self.screen.blit(vertical_speed, (settings.WIDTH - vertical_speed.get_width() - 10, 40))
        self.screen.blit(horizontal_speed, (settings.WIDTH - horizontal_speed.get_width() - 10, 70))
        self.screen.blit(score, (settings.WIDTH - score.get_width() - 10, 100))

        rotated_sprite = pg.transform.rotate(self.lander_sprite, self.lander.rotation)
        new_rect = rotated_sprite.get_rect(center=self.lander_sprite.get_rect(topleft=self.lander.position.to_tuple()).center)
        self.screen.blit(rotated_sprite, new_rect)

    def draw_terrain(self) -> None:
        """
        Draws the terrain
        """
        for i in range(settings.TERRAIN_POINTS_NUMBER):
            if self.terrain.flat_surface_index <= i < self.terrain.flat_surface_index + settings.FLAT_SURFACE_SIZE:
                line_width = 4
            else:
                line_width = 1
            line_start = self.terrain.points[i].to_tuple()
            line_end = self.terrain.points[i + 1].to_tuple()
            pg.draw.line(self.screen, settings.WHITE, line_start, line_end, line_width)

    def run(self):
        """
        Main PyGame loop
        """
        pg.init()
        pg.display.set_caption("Lunar Lander")
        self.font = pg.font.SysFont("courier", 20)
        self.draw_game()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    exit()
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.lander.rotation_direction = 1
            if keys[pg.K_UP]:
                self.lander.thrust = True
            if keys[pg.K_RIGHT]:
                self.lander.rotation_direction = -1
            self.lander.update()
            self.draw_game()
            self.clock.tick(settings.FPS)



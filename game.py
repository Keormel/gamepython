import pygame as pg
import sys
from settings import WIDTH, HEIGHT, FPS
from menu import Menu


class DeathScreen:
    def __init__(self, game, score):
        self.game = game
        self.score = score
        self.font_large = pg.font.Font(None, 96)
        self.font_medium = pg.font.Font(None, 72)
        self.font_small = pg.font.Font(None, 48)
        self.active = True

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN or event.key == pg.K_SPACE:
                    self.active = False

    def draw(self):
        self.game.screen.fill((0, 0, 0))

        # Draw "GAME OVER" text
        game_over_text = self.font_large.render('GAME OVER', True, (255, 0, 0))
        self.game.screen.blit(game_over_text,
                             (WIDTH // 2 - game_over_text.get_width() // 2, 100))

        # Draw final score
        score_label = self.font_medium.render('Final Score:', True, (255, 255, 255))
        self.game.screen.blit(score_label,
                             (WIDTH // 2 - score_label.get_width() // 2, 300))

        score_value = self.font_large.render(str(self.score), True, (0, 255, 0))
        self.game.screen.blit(score_value,
                             (WIDTH // 2 - score_value.get_width() // 2, 400))

        # Draw continue instruction
        continue_text = self.font_small.render('Press ENTER or SPACE to continue', True, (255, 255, 255))
        self.game.screen.blit(continue_text,
                             (WIDTH // 2 - continue_text.get_width() // 2, 650))

        pg.display.flip()

    def run(self):
        while self.active:
            self.handle_events()
            self.draw()
            self.game.clock.tick(FPS)


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.score = 0
        self.show_menu()

    def show_menu(self):
        pg.mouse.set_visible(True)
        pg.event.set_grab(False)
        menu = Menu(self)
        menu.run()
        self.new_game()

    def show_death_screen(self):
        pg.mouse.set_visible(True)
        pg.event.set_grab(False)
        death_screen = DeathScreen(self, self.score)
        death_screen.run()
        menu = Menu(self)
        menu.save_score(self.score)
        menu.run()
        self.new_game()

    def new_game(self):
        from map import Map
        from player import Player
        from object_renderer import ObjectRenderer
        from raycasting import RayCasting
        from object_handler import ObjectHandler
        from weapon import Weapon
        from sound import Sound
        from pathfinding import PathFinding

        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        self.score = 0
        pg.mixer.music.play(-1)
        pg.mouse.set_visible(False)
        pg.event.set_grab(True)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # ...existing code...
        self.object_renderer.draw()
        self.weapon.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.show_death_screen()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
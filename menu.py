import pygame as pg
import sys
from settings import *

class Menu:
    def __init__(self, game):
        self.game = game
        self.font_large = pg.font.Font(None, 72)
        self.font_medium = pg.font.Font(None, 48)
        self.font_small = pg.font.Font(None, 36)
        self.selected = 0
        self.menu_items = ['Start Game', 'Settings', 'Last Score', 'Exit']
        self.last_score = self.load_last_score()
        self.active = True

    def load_last_score(self):
        try:
            with open('last_score.txt', 'r') as f:
                return f.read().strip()
        except:
            return "No score yet"

    def save_score(self, score):
        with open('last_score.txt', 'w') as f:
            f.write(str(score))
        self.last_score = str(score)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.selected = (self.selected - 1) % len(self.menu_items)
                elif event.key == pg.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.menu_items)
                elif event.key == pg.K_RETURN:
                    self.select_item()

    def select_item(self):
        if self.selected == 0:  # Start Game
            self.active = False
        elif self.selected == 1:  # Settings
            self.show_settings()
        elif self.selected == 2:  # Last Score
            self.show_last_score()
        elif self.selected == 3:  # Exit
            pg.quit()
            sys.exit()

    def show_settings(self):
        from settings_menu import SettingsMenu
        settings = SettingsMenu(self.game)
        settings.run()

    def show_last_score(self):
        showing_score = True
        while showing_score:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    showing_score = False

            self.game.screen.fill(BLACK)
            
            title = self.font_large.render('Last Score', True, YELLOW)
            score_text = self.font_medium.render(str(self.last_score), True, GREEN)
            back_text = self.font_small.render('Press any key to go back', True, WHITE)
            
            self.game.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
            self.game.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 300))
            self.game.screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, 600))
            
            pg.display.flip()
            self.game.clock.tick(FPS)

    def draw(self):
        self.game.screen.fill(BLACK)
        
        # Draw title
        title = self.font_large.render('DUNGEON SHOOTER', True, YELLOW)
        self.game.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        # Draw menu items
        for i, item in enumerate(self.menu_items):
            color = YELLOW if i == self.selected else WHITE
            text = self.font_medium.render(item, True, color)
            y_pos = 300 + i * 100
            self.game.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y_pos))
        
        # Draw hint
        hint = self.font_small.render('UP/DOWN to select, ENTER to confirm', True, GRAY)
        self.game.screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 100))
        
        pg.display.flip()

    def run(self):
        while self.active:
            self.handle_events()
            self.draw()
            self.game.clock.tick(FPS)
        return True

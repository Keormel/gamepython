import pygame as pg
import sys
from settings import *

class SettingsMenu:
    def __init__(self, game):
        self.game = game
        self.font_large = pg.font.Font(None, 72)
        self.font_medium = pg.font.Font(None, 48)
        self.font_small = pg.font.Font(None, 36)
        self.selected = 0
        self.settings_items = [
            {'name': 'Master Volume', 'value': 80, 'min': 0, 'max': 100},
            {'name': 'Difficulty', 'value': 1, 'options': ['Easy', 'Normal', 'Hard']},
            {'name': 'Mouse Sensitivity', 'value': 5, 'min': 1, 'max': 10},
            {'name': 'Back to Menu', 'value': None}
        ]
        self.active = True

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.selected = (self.selected - 1) % len(self.settings_items)
                elif event.key == pg.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.settings_items)
                elif event.key == pg.K_LEFT:
                    self.adjust_setting(-1)
                elif event.key == pg.K_RIGHT:
                    self.adjust_setting(1)
                elif event.key == pg.K_RETURN:
                    if self.selected == len(self.settings_items) - 1:
                        self.active = False

    def adjust_setting(self, direction):
        item = self.settings_items[self.selected]
        
        if item['name'] == 'Back to Menu':
            return
        
        if 'min' in item and 'max' in item:
            item['value'] = max(item['min'], min(item['max'], item['value'] + direction * 5))
        elif 'options' in item:
            item['value'] = (item['value'] + direction) % len(item['options'])

    def draw(self):
        self.game.screen.fill(BLACK)
        
        # Draw title
        title = self.font_large.render('Settings', True, YELLOW)
        self.game.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        # Draw settings items
        for i, item in enumerate(self.settings_items):
            color = YELLOW if i == self.selected else WHITE
            
            if item['name'] == 'Back to Menu':
                text = self.font_medium.render(item['name'], True, color)
                self.game.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 300 + i * 100))
            else:
                name_text = self.font_medium.render(item['name'], True, color)
                
                if 'options' in item:
                    value_text = self.font_small.render(item['options'][item['value']], True, color)
                else:
                    value_text = self.font_small.render(str(item['value']), True, color)
                
                name_x = WIDTH // 2 - 400
                value_x = WIDTH // 2 + 200
                y_pos = 300 + i * 100
                
                self.game.screen.blit(name_text, (name_x, y_pos))
                self.game.screen.blit(value_text, (value_x, y_pos))
        
        # Draw hint
        hint = self.font_small.render('UP/DOWN: select | LEFT/RIGHT: adjust | ENTER: confirm', True, GRAY)
        self.game.screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 100))
        
        pg.display.flip()

    def run(self):
        while self.active:
            self.handle_events()
            self.draw()
            self.game.clock.tick(FPS)

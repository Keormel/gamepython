import pygame as pg
from sprite_handler import get_sprite_handler
from constants import WIDTH, HEIGHT

class Weapon:
    def __init__(self, game):
        self.game = game
        self.sprite_handler = get_sprite_handler()
        self.image = self.sprite_handler.create_weapon_sprite(128, 128)
        self.rect = self.image.get_rect()
        self.ammo = 300
        self.max_ammo = 300

    def draw(self):
        """Draw weapon in bottom right corner"""
        self.rect.bottomright = (WIDTH - 10, HEIGHT - 10)
        self.game.screen.blit(self.image, self.rect)
        
        # Draw ammo counter
        font = pg.font.Font(None, 36)
        ammo_text = font.render(f"Ammo: {self.ammo}", True, (255, 255, 0))
        self.game.screen.blit(ammo_text, (WIDTH - 250, HEIGHT - 50))

    def update(self):
        """Update weapon state"""
        pass

    def shoot(self):
        """Handle shooting"""
        if self.ammo > 0:
            self.ammo -= 1
            return True
        return False
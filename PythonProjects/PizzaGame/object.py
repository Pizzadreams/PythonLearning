import pygame
import os

class Object:
    def __init__(self, position, image_filename):
        self.position = position
        self.image = pygame.image.load(os.path.join('assets', image_filename))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

    def update(self):
        # Update object logic goes here
        pass

    def draw(self, screen):
        screen.blit(self.image, self.position)
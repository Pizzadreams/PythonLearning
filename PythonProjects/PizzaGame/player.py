import pygame

class Player:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed

    def update(self):
        # Implement any update logic for the player
        pass

    def draw(self, screen):
        # Implement the logic to draw the player on the screen
        pass

    def handle_input(self):
        # Implement the logic to handle player input (WASD keys)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position[1] -= self.speed
        if keys[pygame.K_s]:
            self.position[1] += self.speed
        if keys[pygame.K_a]:
            self.position[0] -= self.speed
        if keys[pygame.K_d]:
            self.position[0] += self.speed
import pygame

class Player:
    def __init__(self, position, radius, speed):
        self.position = list(position)
        self.radius = radius
        self.speed = speed
        self.rect = pygame.Rect(self.position[0] - radius, self.position[1] - radius, radius * 2, radius * 2)
    def update(self):
        # Implement any update logic for the player
        self.rect.topleft = (self.position[0] - self.radius, self.position[1] - self.radius)

    def draw(self, screen):
        # Implement the logic to draw the player on the screen
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius)

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
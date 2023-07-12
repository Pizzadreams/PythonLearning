import pygame
from player import Player
from object import Object

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600

# Create game window with the specified dimensions
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Pizza Adventure Game")

# Create instances of the Player and Object classes
player = Player((window_width / 2, window_height / 2), 5) # 
pizza = Object((100, 100), "Pizza1.png")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    player.handle_input()
    player.update()

    # Draw game objects
    window.fill((0, 0, 0))  # Clear the window
    player.draw(window)
    pizza.draw(window)

    # Update the display
    pygame.display.flip()

pygame.quit()
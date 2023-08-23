import pygame
from player import Player
from object import Object
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 1000
window_height = 800

# Create game window with the specified dimensions
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Pizza Adventure Game")
pizza_image_path = "assets/Pizza1.png"
pizza_image = pygame.image.load(pizza_image_path)

# Create instances of the Player and Object classes
player = Player((window_width / 2, window_height / 2), 15, 1) # self, position, radius, speed
# pizza = Object((50, 50), "Pizza1.png")

# Get mask for the pizza image
pizza_mask = pygame.mask.from_surface(pizza_image)

# Generate random position for the pizza
pizza_position = (
    random.randint(0, window_width - pizza_image.get_width()),
    random.randint(0, window_height - pizza_image.get_height())
)
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

    # Check for collision with pizza object
    pizza_rect = pizza_image.get_rect(topleft=pizza_position)
    if player.rect.colliderect(pizza_rect):
        # Player has collected the pizza object
        # TODO
        print("Pizza collected!")

    # Draw game objects
    window.fill((2, 0, 121))
    player.draw(window)
    #pizza.draw(window)

    # Draw pizza image
    window.blit(pizza_image, pizza_position)

# Check for collision with the mouse cursor
    mouse_pos = pygame.mouse.get_pos()
    relative_mouse_pos = (mouse_pos[0] - pizza_position[0], mouse_pos[1] - pizza_position[1])

    if 0 <= relative_mouse_pos[0] < pizza_image.get_width() and 0 <= relative_mouse_pos[1] < pizza_image.get_height():
        if pizza_mask.get_at(relative_mouse_pos):
            print("Pizza Collision!")

    # Update the display
    pygame.display.flip()

pygame.quit()
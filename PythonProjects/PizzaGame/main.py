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
    pizza_rect = pizza_image.get_rect(topleft=pizza_position)
    player.handle_input()
    player.update()

    # Draw game objects
    window.fill((2, 0, 121))
    player.draw(window)
   
    # Calculate the player's destination rect (used for collision detection)
    player_dest_rect = pygame.Rect(player.position[0] - player.radius, player.position[1] - player.radius, player.radius * 2, player.radius * 2)
    
    # Check for collision with pizza object via WASD
    if player_dest_rect.colliderect(pizza_rect):
        relative_x = player_dest_rect.left - pizza_position[0]
        relative_y = player_dest_rect.top - pizza_position[1]

        # Check if the relative position is within the bounds of the pizza image
        if 0 <= relative_x < pizza_image.get_width() and 0 <= relative_y < pizza_image.get_height():
            if pizza_mask.get_at((relative_x, relative_y)):
                # Player has collected the pizza object
                print("Pizza collected!")

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
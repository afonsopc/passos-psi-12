import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Load game assets
bird_image = pygame.image.load("bird.png")
bird_rect = bird_image.get_rect()
bird_rect.center = (screen_width // 2, screen_height // 2)

# Game variables
gravity = 0.01
bird_movement = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -2

    # Update game logic
    bird_movement += gravity 
    bird_rect.y += bird_movement

    # Render the game
    screen.fill((255, 255, 255))
    screen.blit(bird_image, bird_rect)

    # Update the display
    pygame.display.flip()

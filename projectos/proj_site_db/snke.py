import pygame
import time
import random

pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Snake initial position and size
snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_size = 10

# Food position
food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Direction
direction = 'RIGHT'
change_to = direction

# Score
score = 0

# Game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_F12:
                score += 100

    # Validate direction
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Update snake position
    if direction == 'RIGHT':
        snake_pos[0][0] += snake_size//2
    if direction == 'LEFT':
        snake_pos[0][0] -= snake_size//2
    if direction == 'UP':
        snake_pos[0][1] -= snake_size//2
    if direction == 'DOWN':
        snake_pos[0][1] += snake_size//2

    # Snake body collision
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over = True

    # Display background
    display.fill(black)

    # Draw snake
    for pos in snake_pos:
        pygame.draw.rect(display, green, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    # Draw food
    pygame.draw.rect(display, red, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    # Snake eats food
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = False

    # Update score
    pygame.display.set_caption("Snake Game | Score: " + str(score))

    # Update display
    pygame.display.flip()

    # Snake eats food
    if snake_pos[0] == food_pos:
        score += 1
        food_spawn = False

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
        food_spawn = True

    # Snake body movement
    snake_pos.insert(0, list(snake_pos[0]))

    # Snake body length control
    if len(snake_pos) > score + 1:
        snake_pos.pop()

    # Game over if snake hits the wall
    if snake_pos[0][0] >= width or snake_pos[0][0] < 0 or snake_pos[0][1] >= height or snake_pos[0][1] < 0:
        game_over = True

    # Delay
    pygame.time.Clock().tick(30)

# Quit the game
pygame.quit()

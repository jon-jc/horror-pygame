# main.py
import pygame
import sys
import random
from player import draw_player, player_pos, player_speed, player_size
from obstacle import draw_obstacle, obstacle_pos, obstacle_speed, obstacle_size
from enemy import draw_enemy, move_enemy, enemy_pos, enemy_speed, enemy_size
from mechanics import detect_collision, player_health, score, WIN_SCORE

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Horror Game")

# Game clock
clock = pygame.time.Clock()

# Main game loop
def game_loop():
    global player_health, score
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
            player_pos[0] += player_speed

        obstacle_pos[1] += obstacle_speed
        if obstacle_pos[1] > SCREEN_HEIGHT:
            obstacle_pos[0] = random.randint(0, SCREEN_WIDTH - obstacle_size)
            obstacle_pos[1] = 0

        enemy_pos = move_enemy(enemy_pos, enemy_speed)

        # Check for collisions
        if detect_collision(player_pos, obstacle_pos, obstacle_size, player_size):
            player_health -= 1
            obstacle_pos[1] = SCREEN_HEIGHT

        if detect_collision(player_pos, enemy_pos, enemy_size, player_size):
            player_health -= 1
            enemy_pos[1] = SCREEN_HEIGHT

        # Clear the screen
        screen.fill(BLACK)

        # Draw the player, obstacle, and enemy
        draw_player(screen, player_pos)
        draw_obstacle(screen, obstacle_pos)
        draw_enemy(screen, enemy_pos)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

        # Check for game over
        if player_health <= 0:
            print("Game Over")
            running = False

        # Check for win condition
        if score >= WIN_SCORE:
            print("You Win!")
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()

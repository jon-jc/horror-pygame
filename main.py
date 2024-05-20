import pygame
import sys
import random
from player import draw_player, player_pos, player_speed, player_size
from environment import draw_environment, environment_update
from enemy import draw_enemy, move_enemy, enemy_pos, enemy_speed, enemy_size
from mechanics import detect_collision, player_health, score, WIN_SCORE, display_text

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
    global player_health, score, enemy_pos
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

        environment_update()
        enemy_pos = move_enemy(enemy_pos, enemy_speed)

        # Check for collisions
        if detect_collision(player_pos, enemy_pos, enemy_size, player_size):
            player_health -= 1
            enemy_pos[1] = SCREEN_HEIGHT
            if player_health <= 0:
                display_text(screen, "You Died!", RED, 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False

        # Clear the screen
        screen.fill(BLACK)

        # Draw elements
        draw_environment(screen)
        draw_player(screen, player_pos)
        draw_enemy(screen, enemy_pos)

        # Display health and score
        display_text(screen, f'Health: {player_health}', WHITE, 24, 10, 10)
        display_text(screen, f'Score: {score}', WHITE, 24, 10, 40)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()

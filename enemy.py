import pygame
import random

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, 750), 0]
enemy_speed = 5

def draw_enemy(screen, enemy_pos):
    pygame.draw.rect(screen, (255, 0, 0), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def move_enemy(enemy_pos, enemy_speed):
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > 600:
        enemy_pos[0] = random.randint(0, 750)
        enemy_pos[1] = 0
    return enemy_pos

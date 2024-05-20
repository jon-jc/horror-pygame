# obstacle.py
import pygame
import random

# Obstacles
obstacle_size = 50
obstacle_pos = [random.randint(0, 750), 0]
obstacle_speed = 10

def draw_obstacle(screen, obstacle_pos):
    pygame.draw.rect(screen, RED, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

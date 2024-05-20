# player.py
import pygame

# Player properties
player_size = 50
player_pos = [400, 550]
player_speed = 5

def draw_player(screen, player_pos):
    pygame.draw.rect(screen, (255, 255, 255), (player_pos[0], player_pos[1], player_size, player_size))

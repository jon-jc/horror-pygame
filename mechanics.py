import pygame

# Player properties
player_health = 3
score = 0
WIN_SCORE = 100

# Collision detection
def detect_collision(player_pos, obj_pos, obj_size, player_size):
    p_x, p_y = player_pos
    o_x, o_y = obj_pos
    if (o_x < p_x < o_x + obj_size or o_x < p_x + player_size < o_x + obj_size) and \
       (o_y < p_y < o_y + obj_size or o_y < p_y + player_size < o_y + obj_size):
        return True
    return False

# Display text
def display_text(screen, text, color, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

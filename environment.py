import pygame

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
DARK_GRAY = (30, 30, 30)
RED = (255, 0, 0)

# Environment properties
lights_off = False
light_timer = 0
light_duration = 120  # 2 seconds

def draw_environment(screen):
    global lights_off
    if lights_off:
        screen.fill(DARK_GRAY)
    else:
        screen.fill((0, 0, 0))

def environment_update():
    global lights_off, light_timer
    light_timer += 1
    if light_timer > light_duration:
        lights_off = not lights_off
        light_timer = 0

def display_text(screen, text, color, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

import pygame
from configuracion import *

def display_timer(screen, elapsed_time):
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f'Time: {elapsed_time}', True, WHITE)
    screen.blit(timer_text, (10, 10))

def display_lives(screen, lives):
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f'Lives: {lives}', True, WHITE)
    screen.blit(lives_text, (SCREEN_WIDTH - 110, 10))

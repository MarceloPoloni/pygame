import pygame
from configuracion import *

def display_timer(screen, elapsed_time):
    """
    Muestra el temporizador en la pantalla.

    Args:
        screen (pygame.Surface): La superficie sobre la que se dibuja el temporizador.
        elapsed_time (int): El tiempo transcurrido en segundos que se mostrará.
    """
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f'Time: {elapsed_time}', True, WHITE)
    screen.blit(timer_text, (10, 10))

def display_lives(screen, lives):
    """
    Muestra la cantidad de vidas restantes en la pantalla.

    Args:
        screen (pygame.Surface): La superficie sobre la que se dibuja la cantidad de vidas.
        lives (int): La cantidad de vidas restantes que se mostrará.
    """
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f'Lives: {lives}', True, WHITE)
    screen.blit(lives_text, (SCREEN_WIDTH - 110, 10))

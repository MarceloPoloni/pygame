import pygame
from configuracion import *

def create_player(x, y):
    """
    Crea un objeto de jugador en una posición específica.

    Args:
        x (int): La coordenada x de la posición inicial del jugador.
        y (int): La coordenada y de la posición inicial del jugador.

    Returns:
        pygame.Rect: Un objeto pygame.Rect que representa al jugador.
    """
    return pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

def move_player(player, dx):
    """
    Mueve al jugador horizontalmente y asegura que no salga de los límites de la pantalla.

    Args:
        player (pygame.Rect): El objeto pygame.Rect que representa al jugador.
        dx (int): La distancia a mover el jugador en el eje x.
    """
    player.x += dx
    if player.left < 0:
        player.left = 0
    if player.right > SCREEN_WIDTH:
        player.right = SCREEN_WIDTH

def draw_player(screen, player):
    """
    Dibuja al jugador en la pantalla.

    Args:
        screen (pygame.Surface): La superficie en la que se dibuja al jugador.
        player (pygame.Rect): El objeto pygame.Rect que representa al jugador.
    """
    pygame.draw.rect(screen, RED, player)

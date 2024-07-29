import pygame
from configuracion import *
from sound import play_block_sound

def create_ball(x, y):
    """
    Crea una bola en una posición específica.

    Args:
        x (int): La coordenada x de la posición inicial de la bola.
        y (int): La coordenada y de la posición inicial de la bola.

    Returns:
        pygame.Rect: Un objeto `pygame.Rect` que representa la bola.
    """
    return pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)

def move_ball(ball, dx, dy):
    """
    Mueve la bola en función de las velocidades dadas.

    Args:
        ball (pygame.Rect): El objeto `pygame.Rect` que representa la bola.
        dx (int): La cantidad de movimiento en la dirección x.
        dy (int): La cantidad de movimiento en la dirección y.
    """
    ball.x += dx
    ball.y += dy

def draw_ball(screen, ball):
    """
    Dibuja la bola en la pantalla.

    Args:
        screen (pygame.Surface): La superficie sobre la que se dibuja la bola.
        ball (pygame.Rect): El objeto `pygame.Rect` que representa la bola.
    """
    pygame.draw.ellipse(screen, WHITE, ball)

def check_collision(ball, player, blocks, dx, dy):
    """
    Verifica las colisiones de la bola con el jugador y los bloques, y ajusta la dirección de la bola en consecuencia.

    Args:
        ball (pygame.Rect): El objeto `pygame.Rect` que representa la bola.
        player (pygame.Rect): El objeto `pygame.Rect` que representa al jugador.
        blocks (list of pygame.Rect): Una lista de objetos `pygame.Rect` que representan los bloques.
        dx (int): La velocidad en la dirección x.
        dy (int): La velocidad en la dirección y.

    Returns:
        tuple: Las nuevas velocidades en las direcciones x e y después de la colisión.
    """
    if ball.colliderect(player):
        dy = -dy
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            dy = -dy
            play_block_sound()
            break
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        dx = -dx
    if ball.top <= 0:
        dy = -dy
    return dx, dy

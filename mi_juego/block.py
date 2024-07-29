import pygame
from configuracion import *
import random

def create_blocks():
    """
    Crea una lista de bloques dispuestos en una cuadrícula.

    Returns:
        list of pygame.Rect: Una lista de objetos `pygame.Rect` que representan los bloques.
    """
    blocks = []
    for x in range(0, BLOCKS_PER_ROW * (BLOCK_WIDTH + 10), BLOCK_WIDTH + 10):
        for y in range(0, ROWS_OF_BLOCKS * (BLOCK_HEIGHT + 10), BLOCK_HEIGHT + 10):
            blocks.append(pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT))
    return blocks

def draw_blocks(screen, blocks):
    """
    Dibuja los bloques en la pantalla.

    Args:
        screen (pygame.Surface): La superficie sobre la que se dibujan los bloques.
        blocks (list of pygame.Rect): Una lista de objetos `pygame.Rect` que representan los bloques.
    """
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)

def move_blocks_down(blocks, dy, screen_height):
    """
    Mueve los bloques hacia abajo y reinicia su posición si salen de la pantalla.

    Args:
        blocks (list of pygame.Rect): Una lista de objetos `pygame.Rect` que representan los bloques.
        dy (int): La cantidad de movimiento en la dirección y.
        screen_height (int): La altura de la pantalla para verificar si un bloque ha salido de la pantalla.
    """
    for block in blocks:
        block.y += dy
        if block.top > screen_height:
            block.y = -BLOCK_HEIGHT
            block.x = random.randint(0, SCREEN_WIDTH - BLOCK_WIDTH)

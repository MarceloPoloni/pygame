import pygame
from configuracion import *
import random

def create_blocks():
    blocks = []
    for x in range(0, BLOCKS_PER_ROW * (BLOCK_WIDTH + 10), BLOCK_WIDTH + 10):
        for y in range(0, ROWS_OF_BLOCKS * (BLOCK_HEIGHT + 10), BLOCK_HEIGHT + 10):
            blocks.append(pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT))
    return blocks

def draw_blocks(screen, blocks):
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)

def move_blocks_down(blocks, dy, screen_height):
    for block in blocks:
        block.y += dy
        if block.top > screen_height:
            block.y = -BLOCK_HEIGHT
            block.x = random.randint(0, SCREEN_WIDTH - BLOCK_WIDTH)
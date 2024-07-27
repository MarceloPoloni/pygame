import pygame
from configuracion import *

def create_player(x, y):
    return pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

def move_player(player, dx):
    player.x += dx
    if player.left < 0:
        player.left = 0
    if player.right > SCREEN_WIDTH:
        player.right = SCREEN_WIDTH

def draw_player(screen, player):
    pygame.draw.rect(screen, RED, player)


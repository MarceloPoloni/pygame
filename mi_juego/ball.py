import pygame
from configuracion import *
from sound import play_block_sound

def create_ball(x, y):
    return pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)

def move_ball(ball, dx, dy):
    ball.x += dx
    ball.y += dy

def draw_ball(screen, ball):
    pygame.draw.ellipse(screen, WHITE, ball)

def check_collision(ball, player, blocks, dx, dy):
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


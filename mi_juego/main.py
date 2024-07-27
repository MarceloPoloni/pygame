import pygame
import sys
import random
from configuracion import *
from player import *
from ball import *
from block import *
from sound import *
from utils import *

pygame.init()


def game_loop():
    global music_volume, sfx_volume, is_muted
    from game_over import game_over_screen

    # Configuración del juego
    clock = pygame.time.Clock()

    # Crear la plataforma
    player = create_player(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - 30)

    # Crear la bola inicial
    balls = [create_ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    ball_velocities = [(5, -5)]

    # Crear los bloques
    blocks = create_blocks()

    # Ajustar el volumen de los sonidos
    set_volume(music_volume, sfx_volume)

    # Reproducir sonido del juego al inicio en bucle
    play_game_music()

    # Temporizador y vidas
    start_ticks = pygame.time.get_ticks()
    lives = 1

    while True:
        screen.fill(BLACK)
        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Clic derecho del mouse
                new_ball = create_ball(player.centerx, player.top - BALL_SIZE // 2)
                balls.append(new_ball)
                ball_velocities.append((5, -5))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            move_player(player, -10)
        if keys[pygame.K_RIGHT]:
            move_player(player, 10)

        for i, ball in enumerate(balls):
            move_ball(ball, *ball_velocities[i])
            ball_velocities[i] = check_collision(ball, player, blocks, *ball_velocities[i])

            if ball.bottom >= SCREEN_HEIGHT:
                lives -= 1
                if lives == 0:
                    game_over_screen(elapsed_time)
                else:
                    balls[i] = create_ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                    ball_velocities[i] = (5, -5)

        move_blocks_down(blocks, 1, SCREEN_HEIGHT)

        draw_player(screen, player)
        for ball in balls:
            draw_ball(screen, ball)
        draw_blocks(screen, blocks)

        display_timer(screen, elapsed_time)
        display_lives(screen, lives)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    from menu import main_menu
    main_menu()

import pygame
import sys
from configuracion import *
from player import *
from ball import *
from block import *
from sound import *
from utils import *
from game_over import game_over_screen

pygame.init()

fondo_green = pygame.transform.scale(pygame.image.load("./src/mi_juego/archivos/green.png"), (800, 600))
fondo_blue = pygame.transform.scale(pygame.image.load("./src/mi_juego/archivos/blue.png"), (800, 600))
fondo_purple = pygame.transform.scale(pygame.image.load("./src/mi_juego/archivos/purple.png"), (800, 600))

pause_imagen = pygame.transform.scale(pygame.image.load("./src/mi_juego/archivos/pausa.jpg"), (200, 100))
mute_imagen = pygame.transform.scale(pygame.image.load("./src/mi_juego/archivos/mute.jpg"), (200, 100))

def get_fondo(name):
    """
    Obtiene el fondo correspondiente según el nombre proporcionado.

    Args:
        name (str): El nombre del fondo (puede ser "green", "blue" o "purple").

    Returns:
        pygame.Surface: La superficie de imagen correspondiente al fondo.
    """
    if name == "green":
        return fondo_green
    elif name == "blue":
        return fondo_blue
    elif name == "purple":
        return fondo_purple

def mute():
    """
    Alterna entre activar y desactivar el sonido. Cuando el sonido está desactivado,
    se silencia tanto la música como los efectos de sonido. Cuando está activado, 
    se restablecen los volúmenes a los valores actuales.
    """
    global is_muted, music_volume, sfx_volume
    if is_muted:
        pygame.mixer.music.set_volume(music_volume)
        for sound in [sonido_juego, sonido_bloque]:
            sound.set_volume(sfx_volume)
        is_muted = False
    else:
        pygame.mixer.music.set_volume(0)
        for sound in [sonido_juego, sonido_bloque]:
            sound.set_volume(0)
        is_muted = True

def game_loop(selected_background):
    """
    Ejecuta el bucle principal del juego. Maneja la lógica del juego, actualiza la pantalla
    y maneja eventos como el movimiento del jugador, la generación de nuevas bolas y la
    verificación de colisiones.

    Args:
        selected_background (str): El nombre del fondo seleccionado para el juego.
    """
    global music_volume, sfx_volume, is_muted
    clock = pygame.time.Clock()
    player = create_player(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - 30)
    balls = [create_ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    ball_velocities = [(5, -5)]
    blocks = create_blocks()

    set_volume(music_volume, sfx_volume)
    play_game_music()

    start_ticks = pygame.time.get_ticks()
    lives = 10
    fondo = get_fondo(selected_background)
    paused = False

    while True:
        screen.blit(fondo, (0, 0))
        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not paused:
                    new_ball = create_ball(player.centerx, player.top - BALL_SIZE // 2)
                    balls.append(new_ball)
                    ball_velocities.append((5, -5))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    mute()
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        pygame.mixer.music.pause()
                        for sound in [sonido_juego, sonido_bloque]:
                            sound.stop()
                    else:
                        pygame.mixer.music.unpause()
                        for sound in [sonido_juego, sonido_bloque]:
                            sound.play()

        if not paused:
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
        else:
            screen.blit(pause_imagen, ((SCREEN_WIDTH - pause_imagen.get_width()) // 2, (SCREEN_HEIGHT - pause_imagen.get_height()) // 2))
        
        if is_muted:
            screen.blit(mute_imagen, (SCREEN_WIDTH - mute_imagen.get_width() - 10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    from menu import main_menu
    main_menu()

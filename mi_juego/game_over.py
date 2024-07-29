import pygame
import sys
from configuracion import *
from menu import main_menu

pygame.font.init()
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

def guardar_puntaje(elapsed_time):
    """
    Guarda el tiempo transcurrido en el archivo `high_scores.csv`.

    Lee las puntuaciones existentes, agrega la nueva puntuación, y guarda las 5 puntuaciones más altas en el archivo.

    Args:
        elapsed_time (int): El tiempo transcurrido que se va a guardar como una nueva puntuación.
    """
    try:
        with open('high_scores.csv', 'r') as file:
            high_scores = [int(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        high_scores = []

    high_scores.append(elapsed_time)
    high_scores = sorted(high_scores, reverse=True)[:5]

    with open('high_scores.csv', 'w') as file:
        for score in high_scores:
            file.write(f'{score}\n')

def game_over_screen(elapsed_time):
    """
    Muestra la pantalla de "Game Over" con el tiempo sobrevivido y el ranking de puntuaciones.

    Muestra el tiempo que el jugador sobrevivió, un mensaje para jugar de nuevo, y el ranking de las 5 puntuaciones más altas.
    Permite al jugador volver al menú principal presionando cualquier tecla.

    Args:
        elapsed_time (int): El tiempo que el jugador sobrevivió en el juego.
    """
    
    global screen

    guardar_puntaje(elapsed_time)

    while True:
        screen.fill(BLACK)
        game_over_text = font.render('Game Over', True, WHITE)
        time_text = small_font.render(f'Time Survived: {elapsed_time} seconds', True, WHITE)
        play_again_text = small_font.render('Press any key to play again', True, WHITE)

        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 150))
        screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, 250))
        screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, 350))

        try:
            with open('high_scores.csv', 'r') as file:
                y_offset = 450
                for i, line in enumerate(file):
                    if line.strip():  
                        score_text = small_font.render(f'{i + 1}. {line.strip()} seconds', True, WHITE)
                        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, y_offset))
                        y_offset += 50
        except FileNotFoundError:
            pass
        except ValueError as e:
            print(f"Error al procesar el archivo de puntuaciones: {e}")

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                main_menu()

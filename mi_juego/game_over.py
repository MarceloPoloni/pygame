import pygame
import json
import sys
from configuracion import *
from menu import main_menu

pygame.font.init()
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

def game_over_screen(elapsed_time):
    try:
        with open('high_scores.json', 'r') as f:
            high_scores = json.load(f)
    except FileNotFoundError:
        high_scores = []

    high_scores.append(elapsed_time)
    high_scores = sorted(high_scores, reverse=True)[:5]

    with open('high_scores.json', 'w') as f:
        json.dump(high_scores, f)

    while True:
        screen.fill(BLACK)
        game_over_text = font.render('Game Over', True, WHITE)
        time_text = small_font.render(f'Time Survived: {elapsed_time} seconds', True, WHITE)
        play_again_text = small_font.render('Press any key to play again', True, WHITE)

        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 150))
        screen.blit(time_text, (SCREEN_WIDTH // 2 - time_text.get_width() // 2, 250))
        screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                main_menu()

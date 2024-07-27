import pygame
import sys
from configuracion import *
from sound import *
from player import *
from ball import *
from block import *
import json

pygame.font.init()
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
MID_ANCHO = SCREEN_WIDTH // 2
MID_ALTO = SCREEN_HEIGHT // 2

BOTON_PLAY_RECT = pygame.Rect(SCREEN_WIDTH // 2  - 150 , SCREEN_HEIGHT // 2 - 100 ,300 , 80)

BOTON_OPTIONS_RECT = pygame.Rect(MID_ANCHO-150,MID_ALTO-5,300,80)

BOTON_TOPS_RECT = pygame.Rect(MID_ANCHO-150,MID_ALTO+90,300,80)

BOTON_CLOSE_RECT = pygame.Rect(MID_ANCHO-150,MID_ALTO+180,300,80)

fondo_menu = pygame.image.load("./src/mi_juego/archivos/fondo.jpg")

def main_menu():
    from main import game_loop
    while True:
        screen.blit(fondo_menu,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        title = font.render('El Bloque', True, BLACK)

        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        crear_boton(screen,BOTON_PLAY_RECT,"JUGAR",font,BLACK,GREEN,RED,pos_mouse)
        crear_boton(screen,BOTON_OPTIONS_RECT,"OPCIONES",font,BLACK,BLUE,WHITE,pos_mouse)
        crear_boton(screen,BOTON_TOPS_RECT,"RANKING",font,BLACK,RED,YELLOW,pos_mouse)
        crear_boton(screen,BOTON_CLOSE_RECT,"CERRAR",font,BLACK,YELLOW,GREEN,pos_mouse)
        

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_PLAY_RECT.collidepoint(pos_mouse):
                    game_loop()
                elif BOTON_OPTIONS_RECT.collidepoint(pos_mouse):
                    config_menu()
                elif BOTON_TOPS_RECT.collidepoint(pos_mouse):
                    show_ranking()

def config_menu():
    global music_volume, sfx_volume

    while True:
        screen.fill(GREEN)
        config_text = font.render('Config Menu', True, BLACK)
        music_volume_text = small_font.render(f'Music Volume: {music_volume:.1f}', True, BLACK)
        sfx_volume_text = small_font.render(f'SFX Volume: {sfx_volume:.1f}', True, BLACK)
        back_button = font.render('Back', True, BLACK)

        screen.blit(config_text, (SCREEN_WIDTH // 2 - config_text.get_width() // 2, 50))
        screen.blit(music_volume_text, (SCREEN_WIDTH // 2 - music_volume_text.get_width() // 2, 200))
        screen.blit(sfx_volume_text, (SCREEN_WIDTH // 2 - sfx_volume_text.get_width() // 2, 300))
        screen.blit(back_button, (SCREEN_WIDTH // 2 - back_button.get_width() // 2, 450))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 450 < event.pos[1] < 450 + back_button.get_height():
                    main_menu()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and music_volume < 1.0:
                    music_volume += 0.1
                elif event.key == pygame.K_DOWN and music_volume > 0.0:
                    music_volume -= 0.1
                elif event.key == pygame.K_RIGHT and sfx_volume < 1.0:
                    sfx_volume += 0.1
                elif event.key == pygame.K_LEFT and sfx_volume > 0.0:
                    sfx_volume -= 0.1

        set_volume(music_volume, sfx_volume)

def show_ranking():
    try:
        with open('high_scores.json', 'r') as f:
            high_scores = json.load(f)
    except FileNotFoundError:
        high_scores = []

    while True:
        screen.fill(YELLOW)
        ranking_text = font.render('Ranking', True, BLACK)
        back_button = font.render('Back', True, BLACK)

        screen.blit(ranking_text, (SCREEN_WIDTH // 2 - ranking_text.get_width() // 2, 50))

        y_offset = 150
        for score in high_scores:
            score_text = small_font.render(f'{score}', True, BLACK)
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, y_offset))
            y_offset += 40

        screen.blit(back_button, (SCREEN_WIDTH // 2 - back_button.get_width() // 2, 450))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 450 < event.pos[1] < 450 + back_button.get_height():
                    main_menu()



def crear_boton(superficie: pygame.Surface, rect: pygame.Rect, texto: str,fuente, color_texto: tuple, color_rect: tuple, color_rect_temp: tuple, pos_mouse: tuple):
    """
    Crea un botón en la superficie especificada.

    Args:
    - superficie (pygame.Surface): La superficie donde se dibujará el botón.
    - rect (pygame.Rect): Rectángulo que define la posición y tamaño del botón.
    - texto (str): Texto que se mostrará en el botón.
    - color_texto (tuple): Color del texto en formato RGB.
    - color_rect (tuple): Color del rectángulo del botón en formato RGB.
    - pos_mouse (tuple): Posición actual del cursor del mouse (x, y).

    Returns:
    bool: True si el mouse está sobre el botón, False en caso contrario.

    Funcionamiento:
    - El botón se dibuja en la superficie con el rectángulo y el texto especificado.
    - Si el cursor del mouse está sobre el botón, el rectángulo se infla (aumenta de tamaño) en 10x10 píxeles.
    - El texto se centra dentro del rectángulo ajustado.
    """
    hover = False
    rect_temporal = rect.copy()

    if rect_temporal.collidepoint(pos_mouse):
        rect_temporal.inflate_ip(10, 10)
        color_rect = color_rect_temp
        hover = True

    pygame.draw.rect(superficie, color_rect, rect_temporal,0,10) 
    superficie_texto = fuente.render(texto, True, color_texto)
    rect_texto = superficie_texto.get_rect(center=rect_temporal.center)

    superficie.blit(superficie_texto, rect_texto)

    return hover



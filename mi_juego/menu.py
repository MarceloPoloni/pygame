import pygame
import sys
from configuracion import *
from sound import *
from player import *
from ball import *
from block import *


pygame.font.init()
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
MID_ANCHO = SCREEN_WIDTH // 2
MID_ALTO = SCREEN_HEIGHT // 2

BOTON_PLAY_RECT = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100, 300, 80)
BOTON_OPTIONS_RECT = pygame.Rect(MID_ANCHO - 150, BOTON_PLAY_RECT.bottom + 10, 300, 80)
BOTON_BACKGROUND_RECT = pygame.Rect(MID_ANCHO - 150, BOTON_PLAY_RECT.bottom + 10, 300, 80)
BOTON_TOPS_RECT = pygame.Rect(MID_ANCHO - 150, BOTON_OPTIONS_RECT.bottom + 10, 300, 80)
BOTON_CLOSE_RECT = pygame.Rect(MID_ANCHO - 150, BOTON_TOPS_RECT.bottom + 10, 300, 80)
BOTON_BACK_RECT = pygame.Rect(MID_ANCHO - 150, BOTON_TOPS_RECT.bottom + 10, 300, 80)
BOTON_BACK_RECT_2 = pygame.Rect(MID_ANCHO - 150, BOTON_BACKGROUND_RECT.bottom + 10, 300, 80)

fondo_menu = pygame.image.load("./src/mi_juego/archivos/fondo.jpg")
selected_background = "blue"
def crear_boton(superficie: pygame.Surface, rect: pygame.Rect, texto: str, fuente, color_texto: tuple, color_rect: tuple, color_rect_temp: tuple, pos_mouse: tuple):
    """
    Crea y dibuja un botón en la superficie especificada.

    El botón cambia de color cuando el ratón está sobre él. Se dibuja un rectángulo con bordes redondeados y se coloca texto en el centro.

    Args:
        superficie (pygame.Surface): La superficie donde se dibuja el botón.
        rect (pygame.Rect): El rectángulo que define la posición y tamaño del botón.
        texto (str): El texto que se mostrará en el botón.
        fuente: La fuente que se usará para renderizar el texto.
        color_texto (tuple): El color del texto del botón.
        color_rect (tuple): El color del rectángulo del botón cuando el ratón no está sobre él.
        color_rect_temp (tuple): El color del rectángulo del botón cuando el ratón está sobre él.
        pos_mouse (tuple): La posición actual del ratón en la pantalla.

    Returns:
        bool: `True` si el ratón está sobre el botón, `False` en caso contrario.
    """
    hover = False
    rect_temporal = rect.copy()

    if rect_temporal.collidepoint(pos_mouse):
        rect_temporal.inflate_ip(10, 10)
        color_rect = color_rect_temp
        hover = True

    pygame.draw.rect(superficie, color_rect, rect_temporal, 0, 10)
    superficie_texto = fuente.render(texto, True, color_texto)
    rect_texto = superficie_texto.get_rect(center=rect_temporal.center)

    superficie.blit(superficie_texto, rect_texto)

    return hover

def main_menu():
    """
    Muestra el menú principal del juego, permitiendo al usuario acceder a las diferentes opciones disponibles:
    Jugar, Opciones, Ranking y Cerrar.

    Al hacer clic en los botones, el juego redirige al usuario a la pantalla correspondiente.
    """
    from main import game_loop
    running = True
    while running:
        screen.blit(fondo_menu, (0, 0))
        pos_mouse = pygame.mouse.get_pos()

        title = font.render('El Bloque', True, BLACK)

        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        crear_boton(screen, BOTON_PLAY_RECT, "JUGAR", font, BLACK, GREEN, RED, pos_mouse)
        crear_boton(screen, BOTON_OPTIONS_RECT, "OPCIONES", font, BLACK, BLUE, WHITE, pos_mouse)
        crear_boton(screen, BOTON_TOPS_RECT, "RANKING", font, BLACK, YELLOW, GREEN, pos_mouse)
        crear_boton(screen, BOTON_CLOSE_RECT, "CERRAR", font, WHITE, RED, BLACK, pos_mouse)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_PLAY_RECT.collidepoint(pos_mouse):
                    game_loop(selected_background)
                elif BOTON_OPTIONS_RECT.collidepoint(pos_mouse):
                    config_menu()
                elif BOTON_BACKGROUND_RECT.collidepoint(pos_mouse):
                    background_menu()
                elif BOTON_TOPS_RECT.collidepoint(pos_mouse):
                    show_ranking()
                elif BOTON_CLOSE_RECT.collidepoint(pos_mouse):
                    pygame.quit()
                    sys.exit()

def background_menu():
    """
    Muestra un menú para que el usuario seleccione el fondo del juego.

    Permite al usuario elegir entre los fondos disponibles: Verde, Azul y Púrpura.
    La selección se realiza al hacer clic en el nombre del fondo, y el fondo seleccionado se guarda en la variable global `selected_background`.
    """
    global selected_background

    backgrounds = ["green", "blue", "purple"]
    background_texts = {
        "green": "Verde",
        "blue": "Azul",
        "purple": "Purpura"
    }
    background_colors = {
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "purple": (128, 0, 128)
    }

    while True:
        screen.blit(fondo_menu, (0, 0))
        pos_mouse = pygame.mouse.get_pos()
        config_text = font.render('Seleccione Fondo', True, BLACK)

        screen.blit(config_text, (SCREEN_WIDTH // 2 - config_text.get_width() // 2, 50))

        y_offset = 200
        for background in backgrounds:
            resaltar_opcion = pos_mouse[1] in range(y_offset, y_offset + 36)
            color_resaltado = background_colors[background] if resaltar_opcion else None
            dibujar_opcion_fondo(screen, background_texts[background], y_offset, color_resaltado)
            y_offset += 100

        crear_boton(screen, BOTON_BACK_RECT, "VOLVER", font, BLACK, YELLOW, GREEN, pos_mouse)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                y_offset = 200
                for background in backgrounds:
                    rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, y_offset, 100, 36)
                    if rect.collidepoint(event.pos):
                        selected_background = background
                    y_offset += 100
                if BOTON_BACK_RECT.collidepoint(pos_mouse):
                    config_menu()

def dibujar_opcion_fondo(superficie, texto, y_offset, color_resaltado):
    """
    Dibuja una opción de fondo en la pantalla.

    Se dibuja un rectángulo resaltado si se pasa un color de resaltado.
    El texto de la opción se dibuja en el centro del rectángulo.

    Args:
        superficie (pygame.Surface): La superficie donde se dibuja la opción.
        texto (str): El texto a mostrar para la opción de fondo.
        y_offset (int): La posición vertical en la superficie para dibujar la opción.
        color_resaltado (tuple): El color del rectángulo de resaltado, si corresponde. Si es None, no se dibuja el resaltado.
    """
    if color_resaltado:
        pygame.draw.rect(superficie, color_resaltado, (SCREEN_WIDTH // 2 - 70, y_offset, 150, 50))
    background_text = small_font.render(texto, True, BLACK)
    rect = background_text.get_rect(center=(SCREEN_WIDTH // 2, y_offset + 18))
    superficie.blit(background_text, rect.topleft)

def config_menu():
    """
    Muestra el menú de configuración del juego.

    Permite ajustar el volumen de la música y los efectos de sonido. También permite cambiar el fondo del juego.
    La configuración se actualiza en tiempo real mediante las teclas de flecha.
    """
    global music_volume, sfx_volume

    while True:
        screen.blit(fondo_menu, (0, 0))
        pos_mouse = pygame.mouse.get_pos()
        config_text = font.render('Config Menu', True, BLACK)
        music_volume_text = small_font.render(f'Music Volume: {music_volume:.1f}', True, BLACK)
        sfx_volume_text = small_font.render(f'SFX Volume: {sfx_volume:.1f}', True, BLACK)

        screen.blit(config_text, (SCREEN_WIDTH // 2 - config_text.get_width() // 2, 50))
        screen.blit(music_volume_text, (SCREEN_WIDTH // 2 - music_volume_text.get_width() // 2, 200))
        screen.blit(sfx_volume_text, (SCREEN_WIDTH // 2 - sfx_volume_text.get_width() // 2, 250))

        crear_boton(screen, BOTON_BACKGROUND_RECT, "FONDO", font, BLACK, RED, YELLOW, pos_mouse)
        crear_boton(screen, BOTON_BACK_RECT_2, "VOLVER", font, BLACK, YELLOW, GREEN, pos_mouse)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_BACK_RECT_2.collidepoint(pos_mouse):
                    main_menu()
                elif BOTON_BACKGROUND_RECT.collidepoint(pos_mouse):
                    background_menu()
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
    """
    Muestra la pantalla de ranking con las puntuaciones más altas guardadas en el archivo `high_scores.csv`.

    Las puntuaciones se muestran en orden descendente. Permite al usuario volver al menú principal.
    """
    try:
        with open('high_scores.csv', 'r') as file:
            # Filtrar líneas vacías y convertir las demás a enteros
            high_scores = [int(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        high_scores = []
    except ValueError as e:
        print(f"Error al procesar el archivo de puntuaciones: {e}")
        high_scores = []

    while True:
        screen.blit(fondo_menu, (0, 0))
        pos_mouse = pygame.mouse.get_pos()
        ranking_text = font.render('Ranking', True, BLACK)

        screen.blit(ranking_text, (SCREEN_WIDTH // 2 - ranking_text.get_width() // 2, 50))

        y_offset = 150
        for score in high_scores:
            score_text = small_font.render(f'{score}', True, BLACK)
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, y_offset))
            y_offset += 40

        crear_boton(screen, BOTON_BACK_RECT, "VOLVER", font, BLACK, YELLOW, GREEN, pos_mouse)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BOTON_BACK_RECT.collidepoint(pos_mouse):
                    main_menu()


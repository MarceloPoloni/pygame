import pygame
import json

pygame.mixer.init()

sonidos = {}

def cargar_sonidos(file_path):
    """
    Carga los sonidos desde un archivo JSON y los almacena en un diccionario global.

    Args:
        file_path (str): La ruta al archivo JSON que contiene la configuración de los sonidos.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
        for name, properties in data['sonidos'].items():
            sound = pygame.mixer.Sound(properties["ruta"])
            sonidos[name] = sound

cargar_sonidos('sonidos.json')

sonido_juego = sonidos.get("sonido_juego")
sonido_bloque = sonidos.get("sonido_bloque")

music_volume = 0.5
sfx_volume = 0.1
is_muted = False

def set_volume(music_vol, sfx_vol):
    """
    Ajusta el volumen de los efectos de sonido y la música.

    Args:
        music_vol (float): El volumen de la música (de 0.0 a 1.0).
        sfx_vol (float): El volumen de los efectos de sonido (de 0.0 a 1.0).
    """
    if sonido_juego:
        sonido_juego.set_volume(music_vol)
    if sonido_bloque:
        sonido_bloque.set_volume(sfx_vol)

def play_game_music():
    """
    Reproduce la música del juego en un bucle continuo si el sonido está disponible.
    """
    if sonido_juego:
        sonido_juego.play(-1)

def play_block_sound():
    """
    Reproduce el sonido del bloque si el sonido está disponible.
    """
    if sonido_bloque:
        sonido_bloque.play()

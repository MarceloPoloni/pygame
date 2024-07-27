import pygame

music_volume = 0.5
sfx_volume = 0.1
is_muted = False

pygame.mixer.init()
sonido_juego = pygame.mixer.Sound("./src/mi_juego/archivos/musica_juego.mp3")
sonido_bloque = pygame.mixer.Sound("./src/mi_juego/archivos/laser_bloque.mp3")

def set_volume(music_vol, sfx_vol):
    sonido_juego.set_volume(music_vol)
    sonido_bloque.set_volume(sfx_vol)

def play_game_music():
    sonido_juego.play(-1)

def play_block_sound():
    sonido_bloque.play()

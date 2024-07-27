import pygame

# Configuración de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Game')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Jugador
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 10

# Bola
BALL_RADIUS = 10
BALL_SIZE = 20

# Bloques
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 20
BLOCKS_PER_ROW = 16
ROWS_OF_BLOCKS = 6

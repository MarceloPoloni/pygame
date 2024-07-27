import pygame
import random
import sys
import json
from settings_juego import *


pygame.init()

# Configurar la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Game')



# Fuente
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Volúmenes iniciales
music_volume = 0.5
sfx_volume = 0.1

# Estado de mute
is_muted = False

# Cargar sonidos
sonido_juego = pygame.mixer.Sound("./src/mi_juego/archivos/musica_juego.mp3")
sonido_bloque = pygame.mixer.Sound("./src/mi_juego/archivos/laser_bloque.mp3")

# Ajustar el volumen de los sonidos
sonido_juego.set_volume(music_volume)
sonido_bloque.set_volume(sfx_volume)

# Función para cargar una imagen en la plataforma
def load_player_image(image_path):
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, (PLAYER_WIDTH, PLAYER_HEIGHT))
    return image


# Pantalla principal

def main_menu():
    while True:
        screen.fill(BLUE)

        title = font.render('CHEL', True, BLACK)
        play_button = font.render('Play', True, BLACK)
        config_button = font.render('Config', True, BLACK)
        ranking_button = font.render('Ranking', True, BLACK)

        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))
        screen.blit(play_button, (SCREEN_WIDTH // 2 - play_button.get_width() // 2, 250))
        screen.blit(config_button, (SCREEN_WIDTH // 2 - config_button.get_width() // 2, 350))
        screen.blit(ranking_button, (SCREEN_WIDTH // 2 - ranking_button.get_width() // 2, 450))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 250 < event.pos[1] < 250 + play_button.get_height():
                    game_loop()
                elif 350 < event.pos[1] < 350 + config_button.get_height():
                    config_menu()
                elif 450 < event.pos[1] < 450 + ranking_button.get_height():
                    show_ranking()



# Función de menú de configuración

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

        # Ajustar volúmenes
        sonido_juego.set_volume(music_volume)
        sonido_bloque.set_volume(sfx_volume)

# Función de menú de ranking

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

# Función para guardar el puntaje
def save_score(score):
    try:
        with open('high_scores.json', 'r') as f:
            high_scores = json.load(f)
    except FileNotFoundError:
        high_scores = []

    high_scores.append(score)
    high_scores = sorted(high_scores, reverse=True)[:10]  # Guardar solo los 10 mejores puntajes

    with open('high_scores.json', 'w') as f:
        json.dump(high_scores, f)

# Función para mostrar el mensaje de Game Over
def game_over_screen(score):
    save_score(score)

    while True:
        screen.fill(RED)
        game_over_text = font.render('Game Over', True, BLACK)
        score_text = small_font.render(f'Your Score: {score}', True, BLACK)
        play_again_text = small_font.render('Play Again', True, BLACK)
        back_button = small_font.render('Main Menu', True, BLACK)

        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 100))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200))
        screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, 300))
        screen.blit(back_button, (SCREEN_WIDTH // 2 - back_button.get_width() // 2, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 300 < event.pos[1] < 300 + play_again_text.get_height():
                    game_loop()
                elif 400 < event.pos[1] < 400 + back_button.get_height():
                    main_menu()

# Función principal del juego
def game_loop():
    global music_volume, sfx_volume, is_muted

    # Configuración del juego
    clock = pygame.time.Clock()

    # Crear la plataforma
    player = pygame.Rect(WIDTH // 2 - PLAYER_WIDTH // 2, HEIGHT - 30, PLAYER_WIDTH, PLAYER_HEIGHT)

    # Crear la bola
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
    ball_dx = 5
    ball_dy = -5

    # Crear los bloques
    blocks = []
    for x in range(0, BLOCKS_PER_ROW * (BLOCK_WIDTH + 10), BLOCK_WIDTH + 10):
        for y in range(0, ROWS_OF_BLOCKS * (BLOCK_HEIGHT + 10), BLOCK_HEIGHT + 10):
            blocks.append(pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT))

    # Ajustar el volumen de los sonidos
    sonido_juego.set_volume(music_volume)
    sonido_bloque.set_volume(sfx_volume)

    # Reproducir sonido del juego al inicio en bucle
    sonido_juego.play(-1)
    
    # Cargar la imagen de fondo del juego
    background_image = pygame.image.load("./src/mi_juego/archivos/descarga.jpeg").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Cargar la imagen de la plataforma
    player_image_path = "./src/mi_juego/archivos/img.png"  
    player_image = load_player_image(player_image_path)

    # Inicializar el puntaje y las vidas
    score = 0
    lives = 3  # Número inicial de vidas
    font = pygame.font.SysFont(None, 36)

    # Inicializar el temporizador
    start_ticks = pygame.time.get_ticks()
    game_duration = 10  # Duración del juego en segundos

    # Función para mostrar el puntaje y las vidas
    def draw_score():
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        timer_text = font.render(f"Time: {game_duration - (pygame.time.get_ticks() - start_ticks) // 1000}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 100, 10))
        screen.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 10))

    # Función para manejar las colisiones de los bloques
    def handle_block_collisions(ball, blocks, ball_dy, score):
        for block in blocks[:]:
            if ball.colliderect(block):
                ball_dy = -ball_dy
                blocks.remove(block)
                score += 1
                if not is_muted:
                    sonido_bloque.play()
                break
        return ball_dy, score

    # Función para manejar las colisiones con la plataforma
    def handle_paddle_collision(ball, player, ball_dy):
        if ball.colliderect(player):
            ball_dy = -ball_dy
        return ball_dy

    # Función para actualizar la posición de los bloques y reiniciarlos si llegan al fondo
    def update_blocks(blocks):
        for block in blocks:
            block.y += BLOCK_FALL_SPEED
            # Reiniciar bloque si llega al fondo
            if block.top >= HEIGHT:
                block.y = random.randint(-BLOCK_HEIGHT * 2, -BLOCK_HEIGHT)
                block.x = random.randint(0, WIDTH - BLOCK_WIDTH)

    # Velocidad de caída de los bloques
    BLOCK_FALL_SPEED = 1

    # Estado de pausa
    is_paused = False

    # Bucle del juego
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = not is_paused
                elif event.key == pygame.K_m:
                    is_muted = not is_muted
                    if is_muted:
                        sonido_juego.set_volume(0)
                        sonido_bloque.set_volume(0)
                    else:
                        sonido_juego.set_volume(music_volume)
                        sonido_bloque.set_volume(sfx_volume)
        
        if not is_paused:
            # Mover la plataforma
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.left > 0:
                player.x -= 10
            if keys[pygame.K_RIGHT] and player.right < WIDTH:
                player.x += 10
                
            # Mover la bola
            ball.x += ball_dx
            ball.y += ball_dy
            
            # Actualizar la posición de los bloques y reiniciarlos si llegan al fondo
            update_blocks(blocks)
            
            # Detectar colisiones con la pantalla
            if ball.left <= 0 or ball.right >= WIDTH:
                ball_dx = -ball_dx
            if ball.top <= 0:
                ball_dy = -ball_dy
            if ball.bottom >= HEIGHT:
                ball_dy = -ball_dy
                # Restablecer la posición de la bola
                ball.x = WIDTH // 2
                ball.y = HEIGHT // 2
                lives -= 1
                score -= 10
                if lives == 0:
                    save_score(score)  # Guardar puntaje cuando el juego termina
                    running = False  # Fin del juego si se acaban las vidas
            
            # Detectar colisiones con la plataforma
            ball_dy = handle_paddle_collision(ball, player, ball_dy)
            
            # Detectar colisiones con los bloques
            ball_dy, score = handle_block_collisions(ball, blocks, ball_dy, score)
            
            # Dibujar todo en la pantalla
            screen.blit(background_image, (0, 0)) 
            screen.blit(player_image, player)
            pygame.draw.ellipse(screen, BALL_COLOR, ball)
            screen.blit(player_image, player)
            for block in blocks:
                pygame.draw.rect(screen, BLOCK_COLOR, block)
            draw_score()
            
            # Actualizar la pantalla
            pygame.display.flip()

            # Comprobar si el tiempo se ha agotado
            if (pygame.time.get_ticks() - start_ticks) // 1000 >= game_duration:
                game_over_screen(score)
                running = False

    sonido_juego.stop()
    main_menu()

if __name__ == '__main__':
    main_menu()
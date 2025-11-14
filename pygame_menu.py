import pygame
import sys

# Inicializar Pygame
pygame.init()

# ----- CONFIGURACIÓN DE LA VENTANA -----
ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pylatro - Menú Principal")

# ----- CARGA DE ASSETS -----
# 🎨 Fondo del menú
fondo_menu = pygame.image.load("Pylatro/wallpaper.jpeg").convert()
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO, ALTO))  # 🔹 Escala al tamaño exacto

# 🎵 Música del menú
pygame.mixer.music.load("Pylatro/balatro.mp3")
pygame.mixer.music.play(-1)

# ----- TEXTOS -----
fuente_titulo = pygame.font.Font(None, 120)
fuente_subtitulo = pygame.font.Font(None, 48)

texto_titulo = fuente_titulo.render("PYLATRO", True, (255, 255, 255))
texto_titulo_rect = texto_titulo.get_rect(center=(ANCHO // 2, ALTO // 3))

texto_iniciar = fuente_subtitulo.render("Presione cualquier tecla para iniciar", True, (255, 255, 255))
texto_iniciar_rect = texto_iniciar.get_rect(center=(ANCHO // 2, ALTO // 1.7))

# ----- BUCLE PRINCIPAL -----
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 🔹 cualquier tecla
            print("✅ Pasando a la siguiente pantalla...")
            running = False  # 🔹 más adelante, reemplazás esto por la siguiente escena

    # Dibujar fondo y textos
    pantalla.blit(fondo_menu, (0, 0))
    pantalla.blit(texto_titulo, texto_titulo_rect)
    pantalla.blit(texto_iniciar, texto_iniciar_rect)

    pygame.display.flip()
    clock.tick(60)

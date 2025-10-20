import pygame
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width,height))
prendido = True
balatroFondo = pygame.image.load("wallpaper.jpeg").convert()
balatroFondo = pygame.transform.scale(balatroFondo, (1280, 480)) 
fuente = pygame.font.SysFont("Times New Roman", 30)
pygame.mixer.music.load("balatro.mp3") 
pygame.mixer.music.play(-1, 0.0) 
pygame.mixer.music.set_volume(1)
x = 0
def dibujar_boton(texto, color, x, y, ancho, alto):
    pygame.draw.rect(screen, color, (x, y, ancho, alto))
    texto_renderizado = fuente.render(texto, True, (255,255,255))
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    screen.blit(texto_renderizado, texto_rect)

while prendido:
    screen.blit(balatroFondo, (width // 2 - balatroFondo.get_width() // 2, height // 2 - balatroFondo.get_height() // 2))
    x +=1
    dibujar_boton("Jugar", (45, 147, 173), width / 2, height / 2, 100, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            prendido = False

    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()

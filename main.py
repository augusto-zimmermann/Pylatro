import pygame
pygame.init()
width = 1366
height = 768
screen = pygame.display.set_mode((1366,768))
prendido = True
balatroFondo = pygame.image.load("wallpaper.jpeg").convert()
balatroFondo = pygame.transform.scale(balatroFondo, (2000, 2000)) 
x = 0
while prendido:
    screen.blit(balatroFondo, (width // 2 - balatroFondo.get_width() // 2, height // 2 - balatroFondo.get_height() // 2))
    x +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prendido = False
        
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()
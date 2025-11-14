import pygame
import sys
import os
from clases import cartas      
import numpy

# --- CONFIGURACIÓN INICIAL ---
pygame.init()
ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ronda de Cartas")
FUENTE = pygame.font.Font(None, 36)

# --- FUNCIONES DE CARTAS ---

def cargar_imagenes_cartas(ruta_base="assets/cartas"):
    """Carga todas las imágenes de cartas desde la carpeta indicada"""
    palos = ["trebol", "picas", "diamantes", "corazones"]
    imagenes = {}

    for palo in palos:
        for valor in range(1, 14):
            nombre_archivo = f"{valor}_{palo}.png"
            ruta = os.path.join(ruta_base, nombre_archivo)
            try:
                img = pygame.image.load(ruta).convert_alpha()
                img = pygame.transform.scale(img, (100, 150))
                imagenes[(valor, palo)] = img
            except:
                print(f"[ADVERTENCIA] No se encontró {ruta}")

    # Cargar dorso
    try:
        dorso = pygame.image.load(os.path.join(ruta_base, "dorso.png")).convert_alpha()
        dorso = pygame.transform.scale(dorso, (100, 150))
    except:
        dorso = None

    imagenes["dorso"] = dorso
    return imagenes


def dibujar_mano(pantalla, mano, seleccionadas, imagenes):
    """Dibuja las cartas en pantalla, con borde verde si están seleccionadas"""
    x_inicio = 150
    y = ALTO // 2
    espacio = 130

    for i, carta in enumerate(mano):
        x = x_inicio + i * espacio
        carta_img = imagenes.get(carta, imagenes["dorso"])
        if i in seleccionadas:
            borde_rect = carta_img.get_rect(topleft=(x - 4, y - 4))
            pygame.draw.rect(pantalla, (0, 255, 0), borde_rect, 4)
        pantalla.blit(carta_img, (x, y))


def dibujar_boton(pantalla, texto, x, y, ancho, alto):
    """Dibuja un botón rectangular con texto"""
    rect = pygame.Rect(x, y, ancho, alto)
    pygame.draw.rect(pantalla, (60, 60, 60), rect)
    pygame.draw.rect(pantalla, (200, 200, 200), rect, 2)
    texto_render = FUENTE.render(texto, True, (255, 255, 255))
    texto_rect = texto_render.get_rect(center=rect.center)
    pantalla.blit(texto_render, texto_rect)
    return rect


# --- INICIALIZACIÓN DE DATOS DEL JUEGO ---
mazo = cartas.crearMazo()
mano_actual = cartas.mano(mazo)
IMAGENES_CARTAS = cargar_imagenes_cartas()

seleccionadas = []
ronda = 1
boton_rect = None

# --- LOOP PRINCIPAL ---
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    pantalla.fill((30, 30, 30))
    texto_ronda = FUENTE.render(f"Ronda {ronda}", True, (255, 255, 255))
    pantalla.blit(texto_ronda, (50, 50))

    # Dibujar mano y botón
    dibujar_mano(pantalla, mano_actual, seleccionadas, IMAGENES_CARTAS)
    boton_rect = dibujar_boton(pantalla, "JUGAR CARTAS", ANCHO // 2 - 100, 100, 200, 60)

    pygame.display.flip()

    # --- EVENTOS ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            break

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            # Click en una carta
            x_inicio = 150
            espacio = 130
            for i in range(len(mano_actual)):
                carta_x = x_inicio + i * espacio
                carta_rect = pygame.Rect(carta_x, ALTO // 2, 100, 150)
                if carta_rect.collidepoint(x, y):
                    if i in seleccionadas:
                        seleccionadas.remove(i)
                    elif len(seleccionadas) < 5:
                        seleccionadas.append(i)

            # Click en el botón "JUGAR CARTAS"
            if boton_rect.collidepoint(x, y) and len(seleccionadas) > 0:
                seleccion = [mano_actual[i] for i in seleccionadas]
                mano_actual, mazo = descartarCartas(mano_actual, mazo, seleccion)
                seleccionadas.clear()
                ronda += 1

    reloj.tick(30)

pygame.quit()
sys.exit()

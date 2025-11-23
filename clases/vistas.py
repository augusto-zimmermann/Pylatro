import math
from typing import List, Tuple, Optional

import pygame

from .cartas import MAX_SELECCION
from .puntaje import valoresDefault


# Config visual / constantes
ANCHO, ALTO = 1280, 720
PANEL_W = 320
COLOR_FONDO = (12, 60, 45)
CARTA_ANCHO, CARTA_ALTO = 120, 174
ALTURA_MANO = 400
LEVANTE_SELECCION = 26
CENTRO_ABANICO_X = int(ANCHO * 0.62)
RADIO_ABANICO = 760
ANGULO_TOTAL = math.radians(50)
BOTON_ANCHO, BOTON_ALTO = 220, 48

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PyLatro")
reloj = pygame.time.Clock()

FUENTE = pygame.font.SysFont("consolas", 22)
FUENTE_CHICA = pygame.font.SysFont("consolas", 16)
FUENTE_GRANDE = pygame.font.SysFont("consolas", 28, bold=True)

SIMBOLO_PALO = {"trebol": "♣", "picas": "♠", "diamantes": "♦", "corazones": "♥"}
COLOR_PALO = {
    "corazones": (205, 50, 50),
    "diamantes": (205, 50, 50),
    "picas": (35, 35, 40),
    "trebol": (30, 110, 30),
}
ETIQUETA_RANGO = {1: "A", 11: "J", 12: "Q", 13: "K"}



# Helpers cartas / mano
def rango_a_texto(r: int) -> str:
    return ETIQUETA_RANGO.get(r, str(r))


def hacer_superficie_carta(carta_tuple: Tuple[int, str], seleccionada: bool = False) -> pygame.Surface:
    # carta base + borde + sombra
    s = pygame.Surface((CARTA_ANCHO + 12, CARTA_ALTO + 12), pygame.SRCALPHA)
    rect = pygame.Rect(6, 6, CARTA_ANCHO, CARTA_ALTO)

    sombra = pygame.Surface((CARTA_ANCHO, CARTA_ALTO), pygame.SRCALPHA)
    pygame.draw.rect(sombra, (0, 0, 0, 120), sombra.get_rect(), border_radius=12)
    s.blit(sombra, (6 + 4, 6 + 6))

    pygame.draw.rect(s, (245, 245, 245), rect, border_radius=12)
    pygame.draw.rect(s, (40, 40, 40), rect, width=2, border_radius=12)

    if seleccionada:
        pygame.draw.rect(s, (250, 220, 80), rect.inflate(8, 8), width=4, border_radius=14)

    rank, suit = carta_tuple
    simbolo = SIMBOLO_PALO.get(suit, "?")
    color = COLOR_PALO.get(suit, (25, 25, 25))
    rango_txt = rango_a_texto(rank)
    texto = FUENTE_GRANDE.render(rango_txt + simbolo, True, color)
    s.blit(texto, (rect.x + 10, rect.y + 8))

    indice_text = FUENTE_CHICA.render(f"{rank}", True, (90, 90, 90))
    s.blit(indice_text, (rect.right - 30, rect.bottom - 24))
    return s


def posiciones_en_abanico(cuantas: int) -> List[Tuple[float, float, float]]:
    pos: List[Tuple[float, float, float]] = []
    if cuantas <= 1:
        pos.append((CENTRO_ABANICO_X - CARTA_ANCHO // 2, ALTURA_MANO - CARTA_ALTO // 2, 0.0))
        return pos

    inicio = -ANGULO_TOTAL / 2
    paso = ANGULO_TOTAL / (cuantas - 1)
    for i in range(cuantas):
        ang = inicio + i * paso
        x = CENTRO_ABANICO_X + math.sin(ang) * RADIO_ABANICO - CARTA_ANCHO // 2
        y = ALTURA_MANO + (1 - math.cos(ang)) * 90 - CARTA_ALTO // 2
        rot = math.degrees(ang) * 0.8
        pos.append((x, y, rot))
    return pos


def dibujar_mano(cartas_en_mano: List[Tuple[int, str]], seleccionadas: List[int]) -> List[pygame.Rect]:
    rects: List[pygame.Rect] = []
    pos = posiciones_en_abanico(len(cartas_en_mano))
    for i in range(len(cartas_en_mano)):
        x, y, rot = pos[i]
        levantar = -LEVANTE_SELECCION if i in seleccionadas else 0
        superficie = hacer_superficie_carta(cartas_en_mano[i], i in seleccionadas)
        rotada = pygame.transform.rotate(superficie, rot)
        rect = rotada.get_rect(center=(x + CARTA_ANCHO // 2 + 6, y + CARTA_ALTO // 2 + 6 + levantar))
        pantalla.blit(rotada, rect)
        rects.append(rect)
    return rects



# HUD y componentes UI
class Boton:
    def __init__(self, rect: pygame.Rect, texto: str, estilo: str = "primario", fuente=None):
        self.rect = rect
        self.texto = texto
        self.estilo = estilo  # primario / peligro / amarillo / mini
        self.fuente = fuente or FUENTE

    def _colores(self, hover: bool):
        if self.estilo == "primario":
            base = (46, 130, 230)
            encima = (70, 165, 255)
            borde = (10, 60, 130)
        elif self.estilo == "peligro":
            base = (210, 70, 70)
            encima = (240, 95, 95)
            borde = (120, 30, 30)
        elif self.estilo == "amarillo":
            base = (225, 160, 60)
            encima = (245, 185, 80)
            borde = (140, 90, 20)
        elif self.estilo == "mini":
            base = (60, 120, 210)
            encima = (80, 150, 240)
            borde = (25, 60, 120)
        else:
            base = (70, 70, 70)
            encima = (95, 95, 95)
            borde = (30, 30, 30)
        return (encima if hover else base), borde

    def dibujar(self, hover: bool = False) -> None:
        color, borde = self._colores(hover)
        pygame.draw.rect(pantalla, color, self.rect, border_radius=12)
        pygame.draw.rect(pantalla, borde, self.rect, width=2, border_radius=12)
        t = self.fuente.render(self.texto, True, (240, 243, 246))
        pantalla.blit(t, t.get_rect(center=self.rect.center))

    def esta_encima(self, pos_mouse) -> bool:
        return self.rect.collidepoint(pos_mouse)

    def clic(self, pos_mouse) -> bool:
        return self.esta_encima(pos_mouse)


def draw_hud(
    estado,
    jugador,
    seleccionadas: List[int],
    ronda_num: int,
    objetivo_siguiente: int,
) -> None:
    panel_rect = pygame.Rect(0, 0, PANEL_W, ALTO)
    pygame.draw.rect(pantalla, (18, 24, 32), panel_rect)
    pygame.draw.rect(pantalla, (40, 48, 60), panel_rect, 2)

    x0 = 20
    y = 18

    titulo = FUENTE_GRANDE.render("PyLatro", True, (245, 245, 245))
    pantalla.blit(titulo, (x0, y))
    y += titulo.get_height() + 6

    ronda_txt = FUENTE_CHICA.render(f"Ronda {ronda_num}", True, (210, 215, 220))
    pantalla.blit(ronda_txt, (x0, y))
    y += ronda_txt.get_height() + 12

    # objetivo
    box_obj = pygame.Rect(x0 - 4, y - 4, PANEL_W - 40, 70)
    pygame.draw.rect(pantalla, (42, 34, 18), box_obj, border_radius=10)
    pygame.draw.rect(pantalla, (120, 90, 40), box_obj, 2, border_radius=10)

    obj_lbl = FUENTE_CHICA.render("Objetivo ronda", True, (245, 230, 180))
    pantalla.blit(obj_lbl, (x0 + 6, y))
    obj_val = FUENTE.render(f"{estado['objetivo']}", True, (245, 80, 80))
    pantalla.blit(obj_val, (x0 + 6, y + 22))
    y += 80

    puntu_lbl = FUENTE_CHICA.render("Puntuación ronda", True, (220, 225, 230))
    pantalla.blit(puntu_lbl, (x0, y))
    y += puntu_lbl.get_height() + 2

    puntos_val = FUENTE.render(str(estado["puntos"]), True, (240, 240, 240))
    pantalla.blit(puntos_val, (x0, y))
    y += puntos_val.get_height() + 16

    # manos / descartes
    caja_md = pygame.Rect(x0 - 4, y - 4, PANEL_W - 40, 64)
    pygame.draw.rect(pantalla, (30, 34, 44), caja_md, border_radius=10)
    pygame.draw.rect(pantalla, (70, 80, 110), caja_md, 1, border_radius=10)

    manos_txt = FUENTE_CHICA.render(f"Manos: {estado['manos_restantes']}", True, (220, 225, 230))
    desc_txt = FUENTE_CHICA.render(f"Descartes: {estado['descartes']}", True, (220, 225, 230))
    pantalla.blit(manos_txt, (x0 + 6, y + 8))
    pantalla.blit(desc_txt, (x0 + 6, y + 32))
    y += 80

    # monedas
    money_lbl = FUENTE_CHICA.render("Monedas", True, (230, 220, 150))
    pantalla.blit(money_lbl, (x0, y))
    y += money_lbl.get_height() + 2

    money_val = FUENTE.render(f"${jugador.dinero}", True, (240, 215, 90))
    pantalla.blit(money_val, (x0, y))
    y += money_val.get_height() + 16

    # seleccionadas
    sel_txt = FUENTE_CHICA.render(
        f"Seleccionadas: {len(seleccionadas)}/{MAX_SELECCION}", True, (210, 215, 220)
    )
    pantalla.blit(sel_txt, (x0, y))


def draw_selected_hand_info(estado, seleccionadas: List[int]) -> None:
    if not seleccionadas:
        return

    mano_actual = estado["mano"]
    seleccion_cartas = [mano_actual[i] for i in seleccionadas if 0 <= i < len(mano_actual)]
    try:
        nombre_jugada, (chips_base, multi_base) = valoresDefault(seleccion_cartas)
    except Exception:
        nombre_jugada, chips_base, multi_base = "N/A", 0, 1

    puntaje_base = chips_base * multi_base

    x0 = 20
    y0 = 430

    box_rect = pygame.Rect(x0 - 4, y0, PANEL_W - 40, 130)
    pygame.draw.rect(pantalla, (24, 26, 34), box_rect, border_radius=10)
    pygame.draw.rect(pantalla, (80, 90, 130), box_rect, 1, border_radius=10)

    titulo = FUENTE_CHICA.render("Jugada actual", True, (225, 225, 235))
    pantalla.blit(titulo, (box_rect.x + 8, box_rect.y + 6))

    nombre = FUENTE_CHICA.render(nombre_jugada, True, (230, 230, 240))
    pantalla.blit(nombre, (box_rect.x + 8, box_rect.y + 30))

    chips_surf = FUENTE.render(str(chips_base), True, (90, 160, 240))
    multi_surf = FUENTE.render(str(multi_base), True, (230, 90, 90))
    x_surf = FUENTE.render("x", True, (235, 235, 235))
    eq_surf = FUENTE.render("=", True, (235, 235, 235))
    total_surf = FUENTE.render(str(puntaje_base), True, (245, 245, 245))

    base_y = box_rect.y + 62
    cx = box_rect.x + 12

    pantalla.blit(chips_surf, (cx, base_y))
    cx += chips_surf.get_width() + 8
    pantalla.blit(x_surf, (cx, base_y))
    cx += x_surf.get_width() + 8
    pantalla.blit(multi_surf, (cx, base_y))
    cx += multi_surf.get_width() + 8
    pantalla.blit(eq_surf, (cx, base_y))
    cx += eq_surf.get_width() + 8
    pantalla.blit(total_surf, (cx, base_y))



# Jokers visibles

def draw_joker_cards(jokers) -> None:
    if not jokers:
        return

    JOKER_W, JOKER_H = 90, 140
    x0 = 340
    y0 = 40
    espacio = 16

    mx, my = pygame.mouse.get_pos()
    hovered_joker = None
    hovered_rect = None

    def colores_para(nombre: str):
        nombre = nombre.lower()
        if "smiley" in nombre:
            return (255, 248, 210), (210, 180, 60)
        if "cavendish" in nombre:
            return (245, 235, 210), (190, 160, 60)
        if "odd" in nombre:
            return (234, 225, 248), (130, 90, 170)
        if "jolly" in nombre:
            return (220, 240, 245), (60, 130, 170)
        return (250, 245, 235), (80, 80, 80)

    for i, jk in enumerate(jokers):
        rect = pygame.Rect(x0 + i * (JOKER_W + espacio), y0, JOKER_W, JOKER_H)
        fondo, borde = colores_para(jk.nombre)

        pygame.draw.rect(pantalla, fondo, rect, border_radius=10)
        pygame.draw.rect(pantalla, borde, rect, 2, border_radius=10)

        nombre = jk.nombre
        if len(nombre) > 9 and " " in nombre:
            parte1, parte2 = nombre.split(" ", 1)
            lineas = [parte1, parte2]
        else:
            lineas = [nombre]

        ty = rect.y + 10
        for linea in lineas:
            surf = FUENTE_CHICA.render(linea, True, borde)
            pantalla.blit(surf, (rect.x + 8, ty))
            ty += surf.get_height() + 2

        label = FUENTE_CHICA.render("JOKER", True, borde)
        pantalla.blit(label, label.get_rect(center=(rect.centerx, rect.bottom - 16)))

        if rect.collidepoint(mx, my):
            hovered_joker = jk
            hovered_rect = rect

    if hovered_joker is not None and hovered_rect is not None:
        desc = hovered_joker.descripcion()
        texto = FUENTE_CHICA.render(desc, True, (235, 235, 235))

        padding = 8
        tooltip_rect = pygame.Rect(
            0,
            0,
            texto.get_width() + padding * 2,
            texto.get_height() + padding * 2,
        )

        tooltip_rect.midtop = (hovered_rect.centerx, hovered_rect.bottom + 8)

        if tooltip_rect.right > ANCHO - 10:
            tooltip_rect.right = ANCHO - 10
        if tooltip_rect.left < 10:
            tooltip_rect.left = 10
        if tooltip_rect.bottom > ALTO - 10:
            tooltip_rect.bottom = ALTO - 10

        pygame.draw.rect(pantalla, (18, 20, 26), tooltip_rect, border_radius=8)
        pygame.draw.rect(pantalla, (90, 100, 130), tooltip_rect, 1, border_radius=8)
        pantalla.blit(texto, (tooltip_rect.x + padding, tooltip_rect.y + padding))


# Tienda UI
def dibujar_tienda(opciones, jugador, mensaje_local: Optional[str] = None):
    pantalla.fill((15, 18, 24))

    titulo = FUENTE_GRANDE.render("TIENDA DE JOKERS", True, (245, 245, 245))
    pantalla.blit(titulo, (60, 26))

    txt_dinero = FUENTE.render(f"Tu dinero: ${jugador.dinero}", True, (240, 225, 120))
    pantalla.blit(txt_dinero, (60, 70))

    y = 130
    mx, my = pygame.mouse.get_pos()
    rects = []

    for jk in opciones:
        width = ANCHO - 120
        item_rect = pygame.Rect(60, y, width, 90)

        hover = item_rect.collidepoint((mx, my))
        fondo = (42, 44, 60) if not hover else (54, 56, 76)
        borde = (120, 120, 150)

        pygame.draw.rect(pantalla, fondo, item_rect, border_radius=12)
        pygame.draw.rect(pantalla, borde, item_rect, 1, border_radius=12)

        nombre_surf = FUENTE.render(jk.nombre, True, (245, 245, 245))
        pantalla.blit(nombre_surf, (item_rect.x + 16, item_rect.y + 10))

        desc_surf = FUENTE_CHICA.render(jk.descripcion(), True, (210, 210, 215))
        pantalla.blit(desc_surf, (item_rect.x + 16, item_rect.y + 40))

        precio_txt = FUENTE_CHICA.render("Precio:", True, (220, 220, 220))
        precio_val = FUENTE_CHICA.render(f"${jk.precio}", True, (240, 225, 120))

        precio_x = item_rect.right - 210
        precio_y = item_rect.y + 14
        pantalla.blit(precio_txt, (precio_x, precio_y))
        pantalla.blit(precio_val, (precio_x + precio_txt.get_width() + 6, precio_y))

        buy_w, buy_h = 110, 36
        buy_rect = pygame.Rect(
            item_rect.right - buy_w - 16,
            item_rect.bottom - buy_h - 12,
            buy_w,
            buy_h,
        )

        puede_pagar = jugador.dinero >= jk.precio
        hover_buy = buy_rect.collidepoint((mx, my))

        if puede_pagar:
            base = (53, 132, 76)
            encima = (71, 160, 101)
        else:
            base = (70, 70, 70)
            encima = (70, 70, 70)

        color_btn = encima if hover_buy and puede_pagar else base
        pygame.draw.rect(pantalla, color_btn, buy_rect, border_radius=10)
        pygame.draw.rect(pantalla, (20, 40, 20), buy_rect, 1, border_radius=10)

        txt_btn = "COMPRAR" if puede_pagar else "SIN FONDOS"
        btn_surf = FUENTE_CHICA.render(txt_btn, True, (245, 245, 245))
        pantalla.blit(btn_surf, btn_surf.get_rect(center=buy_rect.center))

        rects.append((item_rect, buy_rect, jk))
        y += 120

    btn_w, btn_h = 260, 60
    cont_rect = pygame.Rect(60, ALTO - btn_h - 40, btn_w, btn_h)

    hover_cont = cont_rect.collidepoint((mx, my))
    base = (76, 158, 80)
    encima = (96, 184, 102)
    color = encima if hover_cont else base

    pygame.draw.rect(pantalla, color, cont_rect, border_radius=14)
    pygame.draw.rect(pantalla, (35, 90, 40), cont_rect, 2, border_radius=14)

    cont_txt = FUENTE.render("Siguiente Ronda", True, (12, 20, 12))
    pantalla.blit(cont_txt, cont_txt.get_rect(center=cont_rect.center))

    if mensaje_local:
        font_msg = pygame.font.SysFont("consolas", 24, bold=True)
        msg_text = mensaje_local

        color = (245, 245, 245)
        if "Máximo de jokers" in msg_text:
            color = (240, 210, 80)
        elif "No tenés suficiente dinero" in msg_text or "No tenes suficiente dinero" in msg_text:
            color = (230, 70, 70)

        msg_surf = font_msg.render(msg_text, True, color)
        msg_rect = msg_surf.get_rect(center=(ANCHO // 2, ALTO // 2))
        pantalla.blit(msg_surf, msg_rect)

    return rects, cont_rect



# Fondo / decoraciones
def dibujar_fondo() -> None:
    pantalla.fill(COLOR_FONDO)
    capa = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    pygame.draw.circle(capa, (0, 0, 0, 70), (ANCHO // 2, ALTO // 1), 520)
    pygame.draw.circle(capa, (0, 0, 0, 50), (ANCHO * 3 // 4, ALTO * 3 // 4), 360)
    pygame.draw.circle(capa, (0, 0, 0, 40), (ANCHO // 2, ALTO // 3), 260)
    pantalla.blit(capa, (0, 0))

import os
import sys
from typing import List, Optional

import pygame


from clases.Jugador import JugadorModel
from clases.rondas import Ronda
from clases.objetivos import objetivo_ronda
from clases.puntaje import jugarMano
from clases.cartas import recargarMazo, MAX_SELECCION
from clases.Jokers import obtenerListaJokers

from clases.vistas import (
    pantalla,
    reloj,
    ANCHO,
    ALTO,
    dibujar_mano,
    draw_hud,
    draw_selected_hand_info,
    draw_joker_cards,
    Boton,
    dibujar_tienda,
    dibujar_fondo,
    FUENTE,
    FUENTE_CHICA,
    FUENTE_GRANDE,
    BOTON_ANCHO,
    BOTON_ALTO,
)

MAX_RONDAS = 3  # cantidad de rondas para ganar PyLatro

# ---------- Recursos ----------
BASE_DIR = os.path.dirname(__file__)
MAIN_MENU = os.path.join(BASE_DIR, "assets/img/fondo.jpg")

# ---------- Música ----------
MUSIC_GAME = os.path.join(BASE_DIR, "assets/audio/musica_juego.mp3")   
MUSIC_SHOP = os.path.join(BASE_DIR, "assets/audio/musica_shop.mp3")    

pygame.mixer.init()

def reproducir_musica(ruta: str, volumen: float = 0.5):
    if not os.path.isfile(ruta):
        return  # por si falta el archivo, no se rompe el jueguito
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play(-1)  


class BaseState:
    def handle_event(self, event) -> Optional["BaseState"]:
        return None

    def update(self, dt: float) -> Optional["BaseState"]:
        return None

    def draw(self) -> None:
        raise NotImplementedError


class MenuState(BaseState):
    def __init__(self, fondo_path: str):
        base_dir = os.path.dirname(__file__)
        fondo_absoluto = os.path.join(base_dir, fondo_path)

        self.fondo = pygame.image.load(fondo_absoluto).convert()
        self.fondo = pygame.transform.scale(self.fondo, (ANCHO, ALTO))

        self.btn_jugar = Boton(
            pygame.Rect(ANCHO // 2 - 140, ALTO // 2 + 40, 280, 60),
            "Jugar",
            estilo="primario",
        )
        self.btn_salir = Boton(
            pygame.Rect(ANCHO // 2 - 140, ALTO // 2 + 120, 280, 60),
            "Salir",
            estilo="peligro",
        )

        # música de juego/menú
        reproducir_musica(MUSIC_GAME)

    def handle_event(self, event) -> Optional["BaseState"]:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos

            if self.btn_jugar.clic((mx, my)):
                jugador = JugadorModel()
                lista_total_jokers = obtenerListaJokers()
                return GameState(jugador, 1, lista_total_jokers)

            if self.btn_salir.clic((mx, my)):
                pygame.quit()
                sys.exit()

        return None

    def update(self, dt: float) -> Optional["BaseState"]:
        return None

    def draw(self) -> None:
        pantalla.blit(self.fondo, (0, 0))
        mx, my = pygame.mouse.get_pos()
        self.btn_jugar.rect.x = 80
        self.btn_jugar.rect.y = ALTO - 110
        self.btn_jugar.dibujar(self.btn_jugar.esta_encima((mx, my)))

        self.btn_salir.rect.x = ANCHO - 80 - self.btn_salir.rect.width
        self.btn_salir.rect.y = ALTO - 110
        self.btn_salir.dibujar(self.btn_salir.esta_encima((mx, my)))


class GameState(BaseState):
    def __init__(self, jugador: JugadorModel, ronda_num: int, lista_total_jokers):
        self.jugador = jugador
        self.ronda_num = ronda_num
        self.lista_total_jokers = lista_total_jokers

        self.ronda = Ronda(jugador, objetivo_ronda(ronda_num))

        self.seleccionadas: List[int] = []
        self.card_rects: List[pygame.Rect] = []

        self.mensaje_temporal: Optional[str] = None
        self.mensaje_timer: int = 0

        # botones principales
        self.btn_descartar = Boton(
            pygame.Rect(60, ALTO - 80, BOTON_ANCHO, BOTON_ALTO),
            "Descartar selección",
            estilo="peligro",
        )
        self.btn_jugar = Boton(
            pygame.Rect(60 + BOTON_ANCHO + 20, ALTO - 80, BOTON_ANCHO, BOTON_ALTO),
            "Jugar mano",
            estilo="primario",
        )
        self.btn_nuevo = Boton(
            pygame.Rect(ANCHO - 160, ALTO - 60, 140, 40),
            "Nueva partida",
            estilo="mini",
            fuente=FUENTE_CHICA,
        )

        self.btn_orden_valor = Boton(
            pygame.Rect(ANCHO // 2 - 60, ALTO - 130, 90, 36),
            "Valor",
            estilo="amarillo",
            fuente=FUENTE_CHICA,
        )
        self.btn_orden_palo = Boton(
            pygame.Rect(ANCHO // 2 + 40, ALTO - 130, 90, 36),
            "Palo",
            estilo="amarillo",
            fuente=FUENTE_CHICA,
        )

        self.handled_reward = False

    def get_estado(self):
        return {
            "mano": self.ronda.obtenerMano(),
            "mazo": self.ronda.obtenerMazo(),
            "puntos": self.ronda.puntosActuales,
            "objetivo": self.ronda.puntosObjetivo,
            "descartes": self.ronda.descartes,
            "manos_restantes": self.ronda.manosRestantes,
        }

    def descartar_cartas(self, indices: List[int]):
        mano_actual = self.ronda.obtenerMano()
        mazo_actual = self.ronda.obtenerMazo()

        for idx in sorted(indices, reverse=True):
            if 0 <= idx < len(mano_actual):
                mano_actual.pop(idx)

        import random
        for _ in range(len(indices)):
            if not mazo_actual:
                recargarMazo(mazo_actual)
                if not mazo_actual:
                    break
            r = random.randrange(len(mazo_actual))
            mano_actual.append(mazo_actual.pop(r))

        self.ronda.cambiarMano(mano_actual)
        self.ronda.cambiarMazo(mazo_actual)
        self.ronda.disminuirDescartes()

    def jugar_mano(self, indices: List[int]) -> int:
        mano = self.ronda.obtenerMano()
        seleccionadas = [mano[i] for i in indices if 0 <= i < len(mano)]
        puntos = jugarMano(seleccionadas, self.ronda.obtenerJugador().obtenerJokers())
        self.ronda.sumarPuntos(puntos)
        self.ronda.disminuirManosRestantes()

        mano_actual = self.ronda.obtenerMano()
        for idx in sorted(indices, reverse=True):
            if 0 <= idx < len(mano_actual):
                mano_actual.pop(idx)

        mazo_actual = self.ronda.obtenerMazo()
        import random
        for _ in range(len(indices)):
            if not mazo_actual:
                recargarMazo(mazo_actual)
                if not mazo_actual:
                    break
            r = random.randrange(len(mazo_actual))
            mano_actual.append(mazo_actual.pop(r))

        self.ronda.cambiarMano(mano_actual)
        self.ronda.cambiarMazo(mazo_actual)
        return puntos

    def ordenar_por_valor(self):
        mano = self.ronda.obtenerMano()
        mano.sort(key=lambda c: c[0])
        self.ronda.cambiarMano(mano)
        self.seleccionadas.clear()

    def ordenar_por_palo(self):
        orden_palos = {
            "corazones": 0,
            "diamantes": 1,
            "trebol": 2,
            "picas": 3,
        }
        mano = self.ronda.obtenerMano()
        mano.sort(key=lambda c: (orden_palos.get(c[1], 99), c[0]))
        self.ronda.cambiarMano(mano)
        self.seleccionadas.clear()

    def handle_event(self, event) -> Optional["BaseState"]:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos

            clicked_card_index = None
            for i in reversed(range(len(self.card_rects))):
                if self.card_rects[i].collidepoint(mx, my):
                    clicked_card_index = i
                    break

            if clicked_card_index is not None:
                if clicked_card_index in self.seleccionadas:
                    self.seleccionadas.remove(clicked_card_index)
                else:
                    if len(self.seleccionadas) < MAX_SELECCION:
                        self.seleccionadas.append(clicked_card_index)
                    else:
                        self.mensaje_temporal = f"Máximo {MAX_SELECCION} cartas"
                        self.mensaje_timer = 90
                return None

            if self.btn_orden_valor.clic((mx, my)):
                self.ordenar_por_valor()
                return None

            if self.btn_orden_palo.clic((mx, my)):
                self.ordenar_por_palo()
                return None

            if self.btn_descartar.clic((mx, my)):
                if self.seleccionadas and self.ronda.descartes > 0:
                    self.descartar_cartas(self.seleccionadas)
                    self.seleccionadas = []
                    self.mensaje_temporal = "Descartadas"
                    self.mensaje_timer = 90
                else:
                    self.mensaje_temporal = "No podés descartar"
                    self.mensaje_timer = 90

            elif self.btn_jugar.clic((mx, my)):
                if self.seleccionadas:
                    puntos_gan = self.jugar_mano(self.seleccionadas)
                    self.mensaje_temporal = f"Jugaste y ganaste {puntos_gan} pts"
                    self.mensaje_timer = 120
                    self.seleccionadas = []
                else:
                    self.mensaje_temporal = "Seleccioná cartas para jugar"
                    self.mensaje_timer = 90

            elif self.btn_nuevo.clic((mx, my)):
                nuevo_jugador = JugadorModel()
                lista_total_jokers = obtenerListaJokers()
                reproducir_musica(MUSIC_GAME)  # asegurar que vuelve la música de juego
                return GameState(nuevo_jugador, 1, lista_total_jokers)

        return None

    def update(self, dt: float) -> Optional["BaseState"]:
        if self.mensaje_temporal:
            self.mensaje_timer -= 1
            if self.mensaje_timer <= 0:
                self.mensaje_temporal = None

        ronda_terminada = (not self.ronda.quedanManosParaJugar()) or self.ronda.ganaste()

        if ronda_terminada and not self.handled_reward:
            self.handled_reward = True

            if self.ronda.ganaste():
                if self.ronda_num >= MAX_RONDAS:
                    return VictoryState()

                extra = 4 + max(0, self.ronda.manosRestantes)
                self.jugador.dinero += extra
                self.mensaje_temporal = f"GANASTE LA RONDA! +${extra}"
                self.mensaje_timer = 120

                reproducir_musica(MUSIC_SHOP)
                return ShopState(self.jugador, self.ronda_num)

            else:
                return GameOverState("Perdiste la ronda.")

        return None

    def draw(self) -> None:
        dibujar_fondo()
        estado = self.get_estado()
        objetivo_sig = objetivo_ronda(self.ronda_num + 1)

        draw_hud(
            estado,
            self.jugador,
            self.seleccionadas,
            self.ronda_num,
            objetivo_sig,
        )

        self.card_rects = dibujar_mano(estado["mano"], self.seleccionadas)
        draw_selected_hand_info(estado, self.seleccionadas)
        draw_joker_cards(self.jugador.obtenerJokers())

        mx, my = pygame.mouse.get_pos()

        group_rect = pygame.Rect(
            self.btn_orden_valor.rect.x - 24,
            self.btn_orden_valor.rect.y - 18,
            (self.btn_orden_palo.rect.right - self.btn_orden_valor.rect.x) + 48,
            60,
        )
        pygame.draw.rect(pantalla, (20, 70, 40), group_rect, border_radius=12)
        pygame.draw.rect(pantalla, (200, 200, 200), group_rect, 2, border_radius=12)

        titulo = FUENTE_CHICA.render("Ordenar mano", True, (235, 235, 235))
        titulo_rect = titulo.get_rect(
            center=(group_rect.centerx, group_rect.y + 14)
        )
        pantalla.blit(titulo, titulo_rect)

        self.btn_orden_valor.dibujar(self.btn_orden_valor.esta_encima((mx, my)))
        self.btn_orden_palo.dibujar(self.btn_orden_palo.esta_encima((mx, my)))

        self.btn_descartar.dibujar(self.btn_descartar.esta_encima((mx, my)))
        self.btn_jugar.dibujar(self.btn_jugar.esta_encima((mx, my)))
        self.btn_nuevo.dibujar(self.btn_nuevo.esta_encima((mx, my)))

        if self.mensaje_temporal:
            font_msg = pygame.font.SysFont("consolas", 26, bold=True)
            color = (
                (230, 80, 80)
                if "No podés" in self.mensaje_temporal or "Máximo" in self.mensaje_temporal
                else (235, 235, 235)
            )
            msg_surf = font_msg.render(self.mensaje_temporal, True, color)
            msg_rect = msg_surf.get_rect(center=(ANCHO // 2, int(ALTO * 0.18)))
            pantalla.blit(msg_surf, msg_rect)


class ShopState(BaseState):
    def __init__(self, jugador: JugadorModel, ronda_num: int):
        import random

        self.jugador = jugador
        self.ronda_num = ronda_num

        lista_total_jokers = obtenerListaJokers()
        k = min(2, len(lista_total_jokers))
        self.opciones = random.sample(lista_total_jokers, k=k)

        self.shop_message: Optional[str] = None
        self.shop_message_timer: int = 0

        self.shop_rects = []
        self.cont_rect = None

    def handle_event(self, event) -> Optional["BaseState"]:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos

            for rect, buy_rect, jk in self.shop_rects:
                if buy_rect.collidepoint(mx, my):
                    ok, msg = self.jugador.comprar_joker(jk)
                    self.shop_message = msg
                    self.shop_message_timer = 140
                    if ok:
                        self.opciones = [o for o in self.opciones if o is not jk]
                    break

            if self.cont_rect and self.cont_rect.collidepoint(mx, my):
                siguiente_ronda = self.ronda_num + 1
                lista_total_jokers = obtenerListaJokers()
                reproducir_musica(MUSIC_GAME)
                return GameState(self.jugador, siguiente_ronda, lista_total_jokers)

        return None

    def update(self, dt: float) -> Optional["BaseState"]:
        if self.shop_message:
            self.shop_message_timer -= 1
            if self.shop_message_timer <= 0:
                self.shop_message = None
        return None

    def draw(self) -> None:
        self.shop_rects, self.cont_rect = dibujar_tienda(
            self.opciones,
            self.jugador,
            self.shop_message,
        )


class GameOverState(BaseState):
    def __init__(self, texto: str):
        self.texto = texto

    def handle_event(self, event) -> Optional["BaseState"]:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            return MenuState(MAIN_MENU)

        return None

    def update(self, dt: float) -> Optional["BaseState"]:
        return None

    def draw(self) -> None:
        pantalla.fill((18, 20, 24))
        msg = FUENTE_GRANDE.render(self.texto, True, (220, 100, 100))
        info = FUENTE_CHICA.render("Click o tecla para volver al menú.", True, (220, 220, 220))
        pantalla.blit(msg, (ANCHO // 2 - msg.get_width() // 2, ALTO // 2 - 40))
        pantalla.blit(info, (ANCHO // 2 - info.get_width() // 2, ALTO // 2 + 20))


class VictoryState(BaseState):
    def __init__(self):
        self.titulo = "VICTORIA"
        self.texto = "¡Felicitaciones, ganaste PyLatro!"

    def handle_event(self, event) -> Optional["BaseState"]:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            return MenuState(MAIN_MENU)

        return None

    def update(self, dt: float) -> Optional["BaseState"]:
        return None

    def draw(self) -> None:
        pantalla.fill((12, 22, 40))  

        titulo_surf = FUENTE_GRANDE.render(self.titulo, True, (90, 160, 255))
        titulo_rect = titulo_surf.get_rect(center=(ANCHO // 2, ALTO // 2 - 40))
        pantalla.blit(titulo_surf, titulo_rect)

        # texto secundario
        texto_surf = FUENTE_CHICA.render(self.texto, True, (235, 235, 235))
        texto_rect = texto_surf.get_rect(center=(ANCHO // 2, ALTO // 2 + 10))
        pantalla.blit(texto_surf, texto_rect)

        ayuda_surf = FUENTE_CHICA.render(
            "Click o tecla para volver al menú",
            True,
            (200, 200, 200),
        )
        ayuda_rect = ayuda_surf.get_rect(center=(ANCHO // 2, ALTO // 2 + 40))
        pantalla.blit(ayuda_surf, ayuda_rect)


def main():
    current_state: BaseState = MenuState(MAIN_MENU)

    running = True
    while running:
        dt = reloj.tick(60)

        for event in pygame.event.get():
            new_state = current_state.handle_event(event)
            if new_state is not None:
                current_state = new_state

        new_state = current_state.update(dt)
        if new_state is not None:
            current_state = new_state

        current_state.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()

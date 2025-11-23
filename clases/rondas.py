from typing import List, Tuple

from cartas import crearMazo, mano
from jugador import JugadorModel



class Ronda:
    def __init__(self, jugador: JugadorModel, objetivo: int):
        self.puntosActuales: int = 0
        self.puntosObjetivo: int = objetivo
        self.mazo: List[Tuple[int, str]] = crearMazo()
        self.jugador: JugadorModel = jugador
        self.descartes: int = 3
        self.manosRestantes: int = 3
        self.mano: List[Tuple[int, str]] = mano(self.mazo)

    def obtenerMazo(self) -> List[Tuple[int, str]]:
        return self.mazo

    def quedanManosParaJugar(self) -> bool:
        return self.manosRestantes > 0

    def ganaste(self) -> bool:
        return self.puntosActuales >= self.puntosObjetivo

    def quedanDescartes(self) -> bool:
        return self.descartes > 0

    def sumarPuntos(self, puntos: int) -> None:
        self.puntosActuales += puntos

    def obtenerMano(self) -> List[Tuple[int, str]]:
        return self.mano

    def obtenerJugador(self) -> JugadorModel:
        return self.jugador

    def disminuirManosRestantes(self) -> None:
        self.manosRestantes -= 1

    def disminuirDescartes(self) -> None:
        self.descartes -= 1

    def cambiarMano(self, mano_nueva: List[Tuple[int, str]]) -> None:
        self.mano = mano_nueva

    def cambiarMazo(self, mazo_nuevo: List[Tuple[int, str]]) -> None:
        self.mazo = mazo_nuevo

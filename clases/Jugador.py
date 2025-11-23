from typing import List

from .Jokers import Joker


class JugadorModel:
    def __init__(self):
        self.dinero: int = 0
        self.jokers: List[Joker] = []
        self.nivel: int = 1

    def comprar_joker(self, joker: Joker):
        if len(self.jokers) >= 5:
            return False, "Máximo de jokers alcanzado (5)."
        if self.dinero < joker.precio:
            return False, "No tenés suficiente dinero."
        self.jokers.append(joker)
        self.dinero -= joker.precio
        return True, f"Compraste {joker.nombre}."

    def mostrarJokers(self) -> List[str]:
        return [j.nombre for j in self.jokers]

    def obtenerJokers(self) -> List[Joker]:
        return self.jokers


Jugador = JugadorModel

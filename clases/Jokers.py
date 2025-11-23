from typing import List, Tuple


class Joker:
    def __init__(
        self,
        nombre: str,
        multiplicadorAnadir: int,
        chips: int,
        precio: int,
        multiplicador: int,
    ):
        self.nombre = nombre
        self.multiplicadorAnadir = multiplicadorAnadir
        self.chips = chips
        self.precio = precio
        self.multiplicador = multiplicador  

    def habilidad(self, mano: List[Tuple[int, str]] | None = None):
        pass

    def reset(self):
        self.multiplicadorAnadir = 0
        self.chips = 0
        self.multiplicador = 1

    def descripcion(self) -> str:
        return "Joker genérico"

    def __repr__(self) -> str:
        return f"<Joker {self.nombre}>"


class JokerDef(Joker):
    def __init__(self):
        super().__init__("Joker", 4, 0, 4, 1)

    def habilidad(self, mano=None):
        pass

    def reset(self):
        self.multiplicadorAnadir = 4
        self.chips = 0
        self.multiplicador = 1

    def descripcion(self) -> str:
        return "Aumenta en 4 el multiplicador"


class JollyJoker(Joker):
    def __init__(self):
        super().__init__("Jolly Joker", 0, 0, 4, 1)

    def habilidad(self, mano: List[Tuple[int, str]]):
        valores = [v for v, _ in mano]
        contar: dict[int, int] = {}
        for v in valores:
            contar[v] = contar.get(v, 0) + 1
        hay_par = any(c == 2 for c in contar.values())
        if hay_par:
            self.multiplicadorAnadir = 8

    def reset(self):
        self.multiplicadorAnadir = 0
        self.chips = 0
        self.multiplicador = 1

    def descripcion(self) -> str:
        return "Si hay un par, aumenta en 8 el multiplicador"


class SmileyFace(Joker):
    def __init__(self):
        super().__init__("Smiley Face", 0, 0, 6, 1)

    def habilidad(self, mano: List[Tuple[int, str]]):
        cantidad = 0
        for valor, _ in mano:
            if valor > 10:
                cantidad += 1
        if cantidad > 0:
            self.multiplicadorAnadir = 5 * cantidad

    def reset(self):
        self.multiplicadorAnadir = 0
        self.chips = 0
        self.multiplicador = 1

    def descripcion(self) -> str:
        return "Por cada carta J, Q o K aumenta en 5 el multiplicador"


class Cavendish(Joker):
    def __init__(self):
        super().__init__("Cavendish", 0, 0, 10, 3)

    def habilidad(self, mano: List[Tuple[int, str]]):
        pass

    def reset(self):
        self.multiplicadorAnadir = 0
        self.chips = 0
        self.multiplicador = 3

    def descripcion(self) -> str:
        return "Multiplica en 3 el multiplicador (posible destrucción)"


class OddTodd(Joker):
    def __init__(self):
        super().__init__("Odd Todd", 0, 0, 4, 1)

    def habilidad(self, mano: List[Tuple[int, str]]):
        for valor, _ in mano:
            if valor % 2 != 0:
                self.chips = 31
                break

    def reset(self):
        self.multiplicadorAnadir = 0
        self.chips = 0
        self.multiplicador = 1

    def descripcion(self) -> str:
        return "Si la mano tiene al menos una carta impar, suma 31 chips"


def obtenerListaJokers() -> List[Joker]:
    return [JokerDef(), JollyJoker(), SmileyFace(), Cavendish(), OddTodd()]

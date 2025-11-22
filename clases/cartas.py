import random
from typing import List, Tuple

MAX_SELECCION = 5


def crearMazo() -> List[Tuple[int, str]]:
    palos = ["trebol", "picas", "diamantes", "corazones"]
    mazo: List[Tuple[int, str]] = []
    for palo in palos:
        for r in range(1, 14):
            mazo.append((r, palo))
    random.shuffle(mazo)
    return mazo


def mano(mazo: List[Tuple[int, str]], tam: int = 8) -> List[Tuple[int, str]]:
    manoList: List[Tuple[int, str]] = []
    for _ in range(tam):
        if not mazo:
            recargarMazo(mazo)
            if not mazo:
                break
        idx = random.randrange(len(mazo))
        manoList.append(mazo[idx])
        mazo.pop(idx)
    return manoList


def recargarMazo(mazo: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    cartasOrigen = crearMazo()
    for carta in cartasOrigen:
        if carta not in mazo:
            mazo.append(carta)
    random.shuffle(mazo)
    return mazo


def seleccionarCartas_por_indices(
    mano: List[Tuple[int, str]],
    indices: List[int],
) -> List[Tuple[int, str]]:
    seleccion: List[Tuple[int, str]] = []
    for i in indices[:MAX_SELECCION]:
        if 0 <= i < len(mano):
            seleccion.append(mano[i])
    return seleccion


def seleccionarCartas(mano: List[Tuple[int, str]], indices: List[int]) -> List[Tuple[int, str]]:
    return seleccionarCartas_por_indices(mano, indices)


def descartarCartas(
    mano: List[Tuple[int, str]],
    mazo: List[Tuple[int, str]],
    indices_seleccionados: List[int],
):
    for idx in sorted(indices_seleccionados, reverse=True):
        if 0 <= idx < len(mano):
            mano.pop(idx)

    for _ in range(len(indices_seleccionados)):
        if not mazo:
            recargarMazo(mazo)
            if not mazo:
                break
        pos = random.randrange(len(mazo))
        mano.append(mazo[pos])
        mazo.pop(pos)

    return mano, mazo

from typing import List, Tuple

from jokers import Joker

def valoresDefault(manoJugada: List[Tuple[int, str]]):
    if not manoJugada:
        return "Carta Alta", (0, 1)

    valores = [x for x, _ in manoJugada]
    palos = [y for _, y in manoJugada]

    # cuenta repeticiones de valores
    contarNums: dict[int, int] = {}
    for v in valores:
        contarNums[v] = contarNums.get(v, 0) + 1

    hayPar = any(c == 2 for c in contarNums.values())
    num_pares = sum(1 for c in contarNums.values() if c == 2)
    hayTrio = any(c == 3 for c in contarNums.values())
    hayPoker = any(c == 4 for c in contarNums.values())
    hayQuintillo = any(c == 5 for c in contarNums.values())
    hayColor = any(palos.count(p) == 5 for p in palos)
    hayFull = (hayTrio and num_pares == 1)

    # detección de escalera
    listaEsc: List[int] = []
    valores_unicos = sorted(set(valores))
    for x in valores_unicos:
        if all((x + k) in valores_unicos for k in range(5)):
            listaEsc = [x + k for k in range(5)]
            break

    # ranking de jugadas
    if hayQuintillo:
        return "Quintillo", (185 + sum([v for v, c in contarNums.items() if c == 5]), 16)

    if listaEsc and hayColor:
        return "Escalera de Color", (120 + sum(listaEsc), 8)

    if hayPoker:
        return "Poker", (80 + sum([v for v, c in contarNums.items() if c == 4]), 7)

    if hayColor:
        return "Color", (71 + sum(valores), 4)

    if hayFull:
        suma_trio = sum([v for v, c in contarNums.items() if c == 3])
        suma_par = sum([v for v, c in contarNums.items() if c == 2])
        return "Full", (63 + suma_trio + suma_par, 4)

    if listaEsc:
        return "Escalera", (50 + sum(listaEsc), 4)

    if hayTrio:
        suma_trio = sum([v for v, c in contarNums.items() if c == 3])
        return "Trio", (45 + suma_trio, 3)

    if num_pares >= 2:
        return "Doble Par", (25 + sum(contarNums.keys()), 2)

    if hayPar:
        return "Par", (20 + sum(contarNums.keys()), 2)

    return "Carta Alta", (5 + max(valores), 1)


def jugarMano(manoJugada: List[Tuple[int, str]], jokersList: List[Joker]) -> int:
    _, (chipsMano, multiMano) = valoresDefault(manoJugada)

    for jk in jokersList:
        try:
            jk.habilidad(manoJugada)
        except Exception:
            pass
        chipsMano += jk.chips
        multiMano += jk.multiplicadorAnadir * jk.multiplicador
        jk.reset()

    valorFinal = chipsMano * multiMano
    return valorFinal

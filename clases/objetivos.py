
def objetivo_ronda(n: int) -> int:
    bloques = [
        [300, 450, 600],
        [900, 1200, 1500],
        [2100, 2700, 3000],
    ]
    bloque = (n - 1) // 3
    index = (n - 1) % 3

    if bloque < len(bloques):
        return bloques[bloque][index]

    factor = 2 ** (bloque - len(bloques) + 1)
    base = bloques[-1][index] if index < 3 else 300 * (index + 1)
    return base * factor

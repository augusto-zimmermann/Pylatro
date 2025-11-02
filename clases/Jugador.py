
class Jugador():
    def __init__(self,dinero,jokers:list,nivel):
        self.dinero = dinero
        self.jokers = jokers
        self.nivel = nivel

    def comprar_joker(self,joker):
        if self.dinero >= joker.precio:
            self.jokers.append(joker)
            self.dinero -= joker.precio
            print(f"Compraste el joker {joker.nombre}")
        else:
            print("No podés comprarlo amigo")

    def obtenerJokers(self):       #devuelve la lista de jokers
        return self.jokers


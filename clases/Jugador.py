import cartas
import Jokers
listaJokers = []
class Jugador():
    def __init__(self,dinero,cartas,jokers,nivel):
        self.dinero = dinero
        self.cartas = cartas
        self.jokers = jokers
        self.nivel = nivel

    def comprar_joker(self,joker):
        if self.dinero >= joker.precio:
            listaJokers.append(joker)
            self.dinero -= joker.precio
            print(f"Compraste el joker {joker.nombre}")
        else:
            print("No podés comprarlo amigo")

    def devolverJokers(self):       #devuelve la lista de jokers
        return self.jokers

jugador1 = Jugador(4,cartas.cartas,listaJokers,1)
jugador1 = Jugador(4,cartas.crearMazo(),listaJokers,1)

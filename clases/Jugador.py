import cartas
import Jokers
listaJokers = []
class Jugador():
    def __init__(self,dinero,cartas,jokers):
        self.dinero = dinero
        self.cartas = cartas
        self.jokers = jokers
    def comprar_joker(self,joker):
        if self.dinero >= joker.precio:
            listaJokers.append(joker)
        else:
            print("No podés comprarlo amigo")
jugador1 = Jugador(4,cartas.cartas,listaJokers)

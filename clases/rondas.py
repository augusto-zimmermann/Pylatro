import Jugador
import Jokers
import cartas

class Ronda():

    def __init__(self, mazo, roundFinalScore, Jugador):

        self.__mazoOrigen__ = mazo 
        self.mazo = mazo
        self.discards = 4 
        self.handsPlayed = 4
        self.roundScore = 0
        self.roundFinalScore = roundFinalScore
        self.jugador = Jugador
        self.mano = cartas.mano(self.mazo)


    
    def descartar(self):
        if self.discards <= 0:
            print("Ya no te quedan descartes para esta ronda")
            return
        self.discards -= 1
        print("¿Qué cartas querés descartar? Ingresá los índices separados por comas")
        indices = input()
        indicesList = indices.split(",")
        indicesList = [int(i) for i in indicesList]
        self.mano, self.mazo = cartas.descartarCartas(self.mano, self.mazo, indicesList)


def iniciarPartida():
    
    mazo = cartas.crearMazo()
    jugador = Jugador(mazo,4, [])
    ronda = Ronda(mazo, 300, jugador)


# hay que ver como es la logica de la "apuesta", crear un diccionario de valores o alguna forma de 
# identificar puntajes por cada juego de poker, manera de seleccionar las cartas q voy a "apostar"
# (que disminuya el handsplayed), ver si el puntaje es mayor al buscado, capaz no deberia pertenecer a ronda. ver en general
# como se va a jugar la partida en si.

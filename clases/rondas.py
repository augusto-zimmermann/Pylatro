import Jugador
import Jokers
import cartas

class Ronda:
    def __init__(self, puntosActuales:0, puntosObjetivo,mazo,jugador, descartes, manosRestantes):
        self.puntosActuales = puntosActuales
        self.puntosObjetivo = puntosObjetivo
        self.mazo = mazo
        self.jugador = jugador
        self.descartes = descartes
        self.manosRestantes = manosRestantes
     
    def obtenerMazo(self):
         return self.mazo
         
    def quedanManosParaJugar(self):
         return self.manosRestantes > 0
         
    def ganaste(self):
         return self.puntosActuales >= self.puntosObjetivo
       
    def tieneDescartes(self):
         return self.descartes > 0
     
    def sumarPuntos(self, puntos):
         self.puntosActuales += puntos
     
   
def crearRonda(jugador,puntosObjetivo, mazo):
    
    if not mazo:       #si no le paso mazo, lo creo (es por si en algun momento modificamos el mazo pasarselo el modificado)
        mazo = cartas.crearMazo()

    descartes = 3 # en un principio son 3 dps ver si agregamos comodines habria que crear los comodines 
                     # y crear un metodo que sume a los descartes estilo jokers.agregarDescartes

    manosRestantes = 3 #tmb ver si son mas x comodines, etc
       
    ronda = Ronda(0, puntosObjetivo, mazo, jugador, descartes, manosRestantes)
    return ronda
       


def iniciarPartida():
    
    mazo = cartas.crearMazo()
    jugador = Jugador.Jugador(mazo,4, Jugador.listaJokers,1)
    ronda = Ronda(mazo,0, 300, jugador,4,4)
    crearRonda(jugador,ronda.puntosObjetivo,mazo)
iniciarPartida()
# mi idea es un metodo crearRonda que reciba el jugador, objetivo de puntos y mazo por si dps queremos agregar cartas al mazo y returne un obj tipo ronda
# un metodo jugarRonda que reciba esa ronda y la juegue viendo los atributos que tiene usando metodos de la clase y te diga si perdiste o ganaste
# y luego un main que cree las 3 o infinitas rondas.

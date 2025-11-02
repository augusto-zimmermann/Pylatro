import cartas
import Jokers
import Jugador
def finPartidaRutina():
  cartas.recargarMazo()
  Jugador.listaJokers = []
  Jugador.jugador1.nivel = 1
  Jugador.jugador1.dinero = 4
  print("Perdiste! Buena partida")
class Partida():
  def __init__(self,descartesFunc,totalRondas,mano):
    self.descartesFunc = descartesFunc
    self.totalRondas = totalRondas
    self.mano = mano
  def finPartida(self,rondasRest):
    if (self.totalRondas - rondasRest) == self.totalRondas:
      finPartidaRutina()



from clases import cartas
from clases import Jokers
from clases import rondas
from clases import Jugador as j

mazo = cartas.crearMazo()
soyJker = Jokers.Joker("joker",0,0,1,1)
listaJoker = [soyJker]
jugadorYo = j.Jugador(4,listaJoker,1)

ronda = rondas.crearRonda(jugadorYo, 300, mazo)
rondas.jugarRonda(ronda)
# mano = cartas.mano(mazo)
# print(mano)
# seleccionadas = cartas.seleccionarCartas(mano)                  #uso la funcion seleccionar cartas, que te pide una lista de indices.
# print(seleccionadas)
# manoNueva, mazo = cartas.descartarCartas(mano, mazo, seleccionadas)     #si descarta las cartas, descarto y disminuyo los descartes restantes
# print(manoNueva)

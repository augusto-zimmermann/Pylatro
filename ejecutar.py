from clases import rondas
from clases import Jugador as j
from clases import Jokers as jok

import menuInter as m

puntos = 300
aumento = 150
vivo = True
while vivo == True:
    i = 1 # i representa las rondas, si gana 3 aumenta de a pasos mas grandes los puntos
    ante = 0
    print("=========================================")
    if i == 1:
      print(f"Small Blind")
    elif i== 2:
      print(f"Big Blind")
    elif i == 3:
      print(f"Boss Blind")
    elif i == 9:
      print(f"FINAL BLIND")
    print("=========================================")
    rondaActual = rondas.crearRonda(j.jugador1,puntos,False)
    print(f"puntos a alcanzar: {puntos}")
    print(j.jugador1.jokers)

    rondas.jugarRonda(rondaActual)
    if rondaActual.ganaste():
      j.jugador1.dinero += rondaActual.manosRestantes
      print(f"Ha ganado ${rondaActual.manosRestantes}")
      m.menuInter(jok.listaJokersTotal)
      puntos += aumento
      i +=1
    else:
      vivo = False
    if i == 3:
      puntos += aumento * 2
      i = 1
      ante += 1
      print(f"Sube la apuesta a: {ante}/8")

    if ante == 8:
      i = 9
    if ante == 9:
      print("HAS GANADO BALATRO!!!")

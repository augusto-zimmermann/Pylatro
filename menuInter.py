from clases import Jugador
from clases import Jokers as j
import numpy as np
def menuInter(jokers):
  print("======================================")
  print("Menú compras")
  print("======================================")
  print("Elije que joker comprar")
  salir = "N"
  salir = input("Desea salir? Y/N")
  jokerRandom = np.random.randint(0,len(jokers))
  jokerRandom2 = np.random.randint(0,len(jokers))
  comprado = [False,False]
  while salir != 'Y':

    def joker1(comprado):
      if comprado == False:
        print("Joker 1")
        print(jokers[jokerRandom].nombre)
        print(jokers[jokerRandom].precio)
        print(jokers[jokerRandom].descripcion())
    def joker2(comprado):
      if comprado == False:
        print("Joker 2")
        print(jokers[jokerRandom2].nombre)
        print(jokers[jokerRandom2].precio)
        print(jokers[jokerRandom2].descripcion())
    joker1(comprado[0])
    joker2(comprado[1])
    print("Que joker desea comprar?")
    jokerComprar = input()
    
    jokerComprarInt = int(jokerComprar)
    if jokerComprarInt == 1:
      Jugador.jugador1.comprar_joker(jokers[jokerRandom])
      comprado[0] = True
      print(f"tiene {Jugador.jugador1.dinero} dinero restante")

    elif jokerComprarInt == 2:
      Jugador.jugador1.comprar_joker(jokers[jokerRandom2])
      comprado[1] = True
      print(f"tiene {Jugador.jugador1.dinero} dinero restante")

    else:
      print("Presionaste otra tecla no deseada")
    salir = input("Desea salir? Y/N")



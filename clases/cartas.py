import numpy

cantidadCartas = 55

# crea un mazo de cartas y lo devuelve como lista de tuplas mazo = [(1,"picas"),(1,"corazones"),(1,"trebol"), (1,"diamantes")]

def crearMazo():
    cartas =[]
    palo = ["trebol","picas","diamantes","corazones"]
    for i in range(len(palo)):
        for j in range(1,14):
            cartas.append((j,palo[i]))
    return cartas
           
# print(cartas)
mazo = crearMazo()

 # toma 8 cartas random y te devuelve una mano sacandolas del mazo original.
 # la mano es una lista de tuplas igual que el mazo.

def mano(mazo):                                     
    manoList =[]
    for i in range(8):
        random = numpy.random.randint(1,(len(mazo)))
        manoList.append(mazo[random])
        mazo.remove(mazo[random])
    print(manoList)
    return manoList

# le pasas un mazo y lo recarga al normal por si le faltan cartas.

def recargarMazo(mazo):
    cartasOrigen = crearMazo()
    for i in cartasOrigen:
        if i not in mazo:
            mazo.append(i)
    return mazo

#le pasas una mano y la muestra por pantalla
#ej: 1: (3, trebol) 2: (7, corazones), 3: (1, picas) ... para luego el usuario seleccione las cartas por indice 

def mostrarMano(mano):
    for i in range(mano):
        print(f"{i+1}: {mano[i]}")    

# le pasas una mano, el mazo y las cartas a descartar (lista de indices) y te las descarta de la mano
# las elimina del mazo y te devuelve la mano modificada y el mazo modificado
# se va a usar tanto cuando jugas como cuando descartas las cartas ya que luego de jugarlas tambien se "descartan del mazo"

def seleccionarCartas(mano):
    imputUsuario = input()
    indicesSeleccionados = [int(x)-1 for x in imputUsuario.split(",")]               # le resto 1 porque los indices empiezan en 1 en la mano
    indicesSeleccionados =  indicesSeleccionados[:5]                                 # toma hasta 5 cartas seleccionadas si hay menos toma menos
    seleccion = [mano[seleccionada] for seleccionada in indicesSeleccionadas]         # devuelvo una lista con las cartas seleccionadas
    return seleccion


def DescartarCartas(mano,mazo,cartasSeleccionadas):
    for carta in cartasSeleccionadas:
        mano.remove(mano[carta])
      
    #las cartas descartadas se reponen con nuevas cartas del mazo, y son eliminadas del mismo
        
    for i in range(len(cartasSeleccionadas)):
        random = numpy.random.randint(1,(len(mazo)))
        mano.append(mazo[random])
        mazo.remove(mazo[random])

    return mano, mazo 
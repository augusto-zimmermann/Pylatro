import numpy
palo = ["trebol","picas","diamantes","corazones"]
cantidadCartas = 55
cartas =[]
cartasOrigen = []
for i in range(len(palo)):
    for j in range(1,14):
        cartas.append((j,palo[i]))
        cartasOrigen.append(((j,palo[i])))
def mano():
    manoList =[]
    for i in range(8):
        random = numpy.random.randint(1,(len(cartas)))
        manoList.append(cartas[random])
        cartas.remove(cartas[random])
    print(manoList)
    return manoList
mano()
def recargarMazo(mazo):
    for i in cartasOrigen:
        if i not in mazo:
            mazo.append(i)
    return mazo
# recargarMazo(cartas)

import tablaValores as tabla
#jugada se refiere a la manoJugada = (3, trebol), (4, diamante)... etc

def valorFinal(manoJugada,jokersList):
    #jugada = [(1,)]
    valorFinal = 0
    chipsMano = tabla.valoresDefault(manoJugada)[1][0]
    multiMano = tabla.valoresDefault(manoJugada)[1][1]
    for i in jokersList:

        i.habilidad(manoJugada)
        chipsMano += i.chips
        multiMano += i.multiplicadorAnadir * i.multiplicador
        i.reset()        #resetea los multiplicadores despues.

    valorFinal = chipsMano * multiMano
    return valorFinal


#jugada se refiere a la manoJugada = (3, trebol), (4, diamante)... etc
#devuelve el valor final de la mano jugada con los jokers aplicados a la mano
def valoresDefault(manoJugada): #mano jugada: [(1,"trebol"),(2,"diamantes")]

    valores = [x for x, y in manoJugada]
    palos = [y for x, y in manoJugada]

    # Contar ocurrencias de cada valor
    contarNums = {}
    for x in valores:
        contarNums[x] = contarNums.get(x, 0) + 1 #cuenta la cantidad de veces que aparece un numero

    # Tipos de jugadas
    hayPar = any(x == 2 for x in contarNums.values()) # any () devuelve booleano
    hayParList = [x == 2 for x in contarNums.values()]
    hay2Par = sum(1 for x in contarNums.values() if x == 2) # {1: 1, 4:2, 5:2}
    hayTrio = [x for x, c in contarNums.items() if c == 3]
    hayPoker = [x for x, c in contarNums.items() if c == 4]
    hayQuintillo = [x for x, c in contarNums.items() if c == 5]
    hayColor = any(palos.count(p) == 5 for p in palos)
    hayFull = (len(hayTrio) == 1 and hay2Par == 1)
    listaEsc = []
    for x in sorted(valores):
      if (x+1 in valores) and (x+2 in valores) and (x+3 in valores) and (x+4 in valores):
        listaEsc.append(x)
        listaEsc.append(x+1)
        listaEsc.append(x+2)
        listaEsc.append(x+3)
        listaEsc.append(x+4) 
        
    if hayQuintillo:
        return "Quintillo", ((185 + sum(hayQuintillo)) , 16) 
    elif listaEsc and hayColor:
        return "Escalera de Color", (120 + sum(listaEsc), 8)
    elif hayPoker:
        return "Poker", ((80 + sum(hayPoker)) , 7)
    elif hayColor:
        return "Color", ((71 + sum(valores)) , 4)
    elif hayFull:
        return "Full",((63 + sum(hayTrio) + sum(hayParList)) , 4)
    elif listaEsc:
        return "Escalera", ((50 + sum(listaEsc)) , 4)
    elif hayTrio:
        return "Trio", ((45 + sum(hayTrio)) , 3)
    elif hay2Par:
        return "Doble Par",((25 + sum(contarNums.keys())), 2)
    elif hayPar:
        return "Par" ,((20 + sum(contarNums.keys())) , 2)
    else:
        return "Carta Alta", (5 + max(valores),1)
    


def jugarMano(manoJugada,jokersList):
    #jugada = [(1,)]
    valorFinal = 0
    chipsMano = valoresDefault(manoJugada)[1][0]
    multiMano = valoresDefault(manoJugada)[1][1]
    for i in jokersList:

        i.habilidad(manoJugada)
        chipsMano += i.chips
        multiMano += i.multiplicadorAnadir * i.multiplicador
        i.reset()        #resetea los multiplicadores despues.

    valorFinal = chipsMano * multiMano
    return valorFinal
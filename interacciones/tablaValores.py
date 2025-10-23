def valoresDefault(manoJugada): #mano jugada: [(1,"trebol"),(2,"diamantes")]

    valores = [x for x, y in manoJugada]
    palos = [y for x, y in manoJugada]

    # Contar ocurrencias de cada valor
    contarNums = {}
    for x in valores:
        contarNums[x] = contarNums.get(x, 0) + 1 #cuenta la cantidad de veces que aparece un numero

    # Tipos de jugadas
    hayPar = any(x == 2 for x in contarNums.values()) # any () devuelve booleano
    hay2Par = sum(1 for x in contarNums.values() if x == 2)
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

    jugadas = {}

    if hayPar and hay2Par != 2:
        jugadas["Par"] = (20 + sum(contarNums.keys())) * 2
    if hay2Par == 2 and not hayFull:
        jugadas["Doble Par"] = (25 + sum(contarNums.keys())) * 2
    if hayTrio:
        jugadas["Trio"] = (45 + sum(hayTrio)) * 3
    if hayPoker:
        jugadas["Poker"] = (80 + sum(hayPoker)) * 7
    if hayQuintillo:
        jugadas["Quintillo"] = (185 + sum(hayQuintillo)) * 16
    if hayColor and not listaEsc:
        jugadas["Color"] = (71 + sum(valores)) * 4
    if hayFull:
        jugadas["Full"] = (63 + sum(hayTrio)) * 4
    if listaEsc and not hayColor:
        jugadas["Escalera"] = (50 + sum(listaEsc)) * 4
    if listaEsc and hayColor:
        jugadas["Escalera de Color"] = (120 + sum(listaEsc)) * 8
    jugadas["Carta Alta"] = (5 + max(valores))
    nombreJugada = max(jugadas, key=jugadas.get)
    valorJugadaDef = jugadas[nombreJugada]

    return (valorJugadaDef, nombreJugada)

print(valoresDefault(manoJugada))

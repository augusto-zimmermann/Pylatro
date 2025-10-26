from clases import Jugador
from clases import Jokers
from clases import cartas

class Ronda:
    def _init_(self, puntosActuales, puntosObjetivo,mazo,jugador, descartes, manosRestantes):
        self.puntosActuales = 0
        self.puntosObjetivo = puntosObjetivo
        self.mazo = mazo
        self.jugador = jugador
        self.descartes = descartes
        self.manosRestantes = manosRestantes
        self.mano = cartas.mano(mazo)
     
    def obtenerMazo(self):
         return self.mazo
         
    def quedanManosParaJugar(self):
         return self.manosRestantes > 0
         
    def ganaste(self):
         return self.puntosActuales >= self.puntosObjetivo
       
    def quedanDescartes(self):
         return self.descartes > 0
     
    def sumarPuntos(self, puntos):
         self.puntosActuales += puntos

    def obtenerMano(self):
        return self.mano

    def mostrarMano(self):
        cartas.mostrarMano(self.mano)

    def obtenerJokers(self)
        return self.jugador.devolverJokers()            #deberia funcionar nose como relacionar los archivos

    def disminuirManosRestantes(self):
        self.manosRestantes -= 1

    def disminuirDescartes(self):
        self.descartes -=1

     
   
def crearRonda(jugador,puntosObjetivo, mazo):
    
    if not mazo:       #si no le paso mazo, lo creo (es por si en algun momento modificamos el mazo pasarselo el modificado)
        mazo = cartas.crearMazo()

    descartes = 3 # en un principio son 3 dps ver si agregamos comodines habria que crear los comodines 
                     # y crear un metodo que sume a los descartes estilo jokers.agregarDescartes

    manosRestantes = 3 #tmb ver si son mas x comodines, etc
       
    ronda = Ronda(0, puntosObjetivo, mazo, jugador, descartes, manosRestantes)
    return ronda
       

def jugarRonda(ronda->Ronda):

    copiaMazo = ronda.obtenerMazo()  #lo copio porque en la ronda se va a modificar y luego lo necesito para la proxima ronda.

    while ronda.quedanManosParaJugar() and not ronda.ganaste(): #si no ganaste y quedan manos para jugar te pregunta que hacer
        
        ronda.mostrarMano()

        if  ronda.quedanDescartes():        #si quedan descartes le ofrece las dos opciones
            print("seleccione cartas por indice hasta 5, separadas por comas, para descartarlas o jugar la mano")
            seleccionadas = cartas.seleccionarCartas(ronda.devolverMano())
            opcion = "todavia sin ingresar"

            while opcion != "1" or opcion != "2":
                print("desea \n1: descartar las cartas seleccionadas\n2:jugar las cartas seleccionadas")
                opcion = input()[0]
                if opcion == "1"
                    seleccionadas = cartas.seleccionarCartas(ronda.devolverMano())                  #uso la funcion seleccionar cartas, que te pide una lista de indices.
                    cartas.descartarCartas(ronda.obtenerMano(), ronda.obtenerMazo(), seleccionadas) #si descarta las cartas, descarto y disminuyo los descartes restantes
                    ronda.disminuirDescartes()
                elif opcion == "2"
                    seleccionadas = cartas.seleccionarCartas(ronda.devolverMano())
                    puntosASumar = jugarMano.jugarMano(seleccionadas, ronda.obtenerJokers())        #si juega la mano sumo los puntos y disminuyo las manos jugadas restantes
                    ronda.sumarPuntos(puntosASumar)
                    ronda.disminuirManosRestantes()
                    cartas.descartarCartas(ronda.obtenerMano(), ronda.obtenerMazo(), seleccionadas)
                else:
                    print("intentelo de nuevo con una opcion posible")

        else:               #si no quedan descartes solo puede jugar la mano
            print("seleccione cartas por indice hasta 5, separadas por comas, para jugar la mano")
            seleccionadas = cartas.seleccionarCartas(ronda.devolverMano())
            puntosASumar = jugarMano.jugarMano(seleccionadas, ronda.obtenerJokers())
            ronda.sumarPuntos(puntosASumar)
            ronda.disminuirManosRestantes()
            cartas.descartarCartas(ronda.obtenerMano(), ronda.obtenerMazo(), seleccionadas)
            

    if ronda.ganaste():
        print("¡Has ganado la ronda!")      #imprime si gano o pierdo la ronda
    else:                                                           
        print("No te quedan manos. Has perdido la ronda.")

    return ronda.ganaste()      #devuelve el booleano si gano para saber si jugare la proxima ronda o no 
            
    

def iniciarPartida():
    
    mazo = cartas.crearMazo()
    jugador = Jugador(mazo,4, [])
    ronda = Ronda(mazo, 300, jugador)


# mi idea es un metodo crearRonda que reciba el jugador, objetivo de puntos y mazo por si dps queremos agregar cartas al mazo y returne un obj tipo ronda
# un metodo jugarRonda que reciba esa ronda y la juegue viendo los atributos que tiene usando metodos de la clase y te diga si perdiste o ganaste
# y luego un main que cree las 3 o infinitas rondas.
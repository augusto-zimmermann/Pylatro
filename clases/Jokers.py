
class Joker():
    def __init__(self,nombre:str,multiplicadorAnadir:int,chips:int,precio:int,multiplicador:int):
        self.nombre = nombre
        self.multiplicadorAnadir = multiplicadorAnadir
        self.chips = chips 
        self.precio = precio
        self.multiplicador = multiplicador # 10 X 4 -> 10 X (4*multiplicador)
    def habilidad(self,mano=None): 
        pass
    def reset(self):
      self.multiplicadorAnadir = 4
      self.chips = 0
      self.multiplicador = 1
    def descripcion(self):
      desc = print("Este Joker aumenta en 4 el multiplicador")
      return desc
JokerDef = Joker("Joker",4,0,4,1)

class JollyJoker(Joker):
    def __init__(self,nombre:str,multiplicadorAnadir:int,chips:int,precio:int,multiplicador:int):
        super().__init__(nombre,multiplicadorAnadir,chips,precio,multiplicador)
    def habilidad(self,mano):
        for i in mano:
            if i[0] in mano:
                self.multiplicadorAnadir = 8
    def reset(self):
      self.multiplicadorAnadir = 0
      self.chips = 0
      self.multiplicador = 1
    def descripcion(self):
      desc = print("Si hay un par aumenta en 8 el multiplicador")
      return desc
jollyJoker = JollyJoker("Jolly Joker",0,0,4,1)
class SmileyFace(Joker):
    def __init__(self,nombre:str,multiplicadorAnadir:int,chips:int,precio:int,multiplicador:int):
        super().__init__(nombre,multiplicadorAnadir,chips,precio,multiplicador)
    def habilidad(self,mano):
        for i in mano:
            if i[0] > 10:
                self.multiplicadorAnadir = 5
    def reset(self):
      self.multiplicadorAnadir = 0
      self.chips = 0
      self.multiplicador = 1
    def descripcion(self):
      desc = print("Por cada carta 11,12 o 13 aumenta en 5 el multiplicador")
      return desc
smileyFace = SmileyFace("Smiley Face",0,0,6,1)
class Cavendish(Joker):
    def __init__(self,nombre:str,multiplicadorAnadir:int,chips:int,precio:int,multiplicador:int):
        super().__init__(nombre,multiplicadorAnadir,chips,precio,multiplicador)
    def habilidad(self,mano):
        pass 
    def reset(self):
      self.multiplicadorAnadir = 0
      self.chips = 0
      self.multiplicador = 3
    def descripcion(self):
      desc = print("Multiplica en 3 el multiplicador, chance de destruirse de 1/1000")
      return desc
cavendish = Cavendish("Cavendish",0,0,10,3)
class OddTodd(Joker):
    def __init__(self,nombre:str,multiplicadorAnadir:int,chips:int,precio:int,multiplicador:int):
        super().__init__(nombre,multiplicadorAnadir,chips,precio,multiplicador)
    def habilidad(self,mano):
        for i in mano:
            if i[0] %2 !=0:
                self.chips = 31
    def reset(self):
      self.multiplicadorAnadir = 0
      self.chips = 0
      self.multiplicador = 1
    def descripcion(self):
      desc = print("Si la mano jugada contiene al menos una carta impar aumenta en 31 las chips")
      return desc
oddTodd = OddTodd("Odd Todd",0,0,4,1)
listaJokersTotal = [JokerDef,jollyJoker,smileyFace,cavendish,oddTodd]

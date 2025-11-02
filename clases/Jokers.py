
class Joker():
    def __init__(self,nombre:str,multiplicadorAnadir:int,chips:int,precio:int,multiplicador:int):
        self.nombre = nombre
        self.multiplicadorAnadir = multiplicadorAnadir
        self.chips = chips 
        self.precio = precio
        self.multiplicador = multiplicador # 10 X 4 -> 10 X (4*multiplicador)
    def habilidad(self): 
        pass
    def reset(self):
      self.multiplicadorAnadir = 4
      self.chips = 0
      self.multiplicador = 1
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
Cavendish = Cavendish("Cavendish",0,0,10,3)
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
oddTodd = OddTodd("Odd Todd",0,0,4,1)

import math

class Rectangulo:
    def __init__(self, punto1 = (0,0), punto2 = (0,0)):
        self.punto1 = punto1
        self.punto2 = punto2
    
    def distancia(self):
      distancia = 0
      if self.punto1[0]>self.punto2[0]:
        distancia = math.sqrt(math.pow(self.punto1[0]-self.punto2[0],2)+math.pow(self.punto1[1]-self.punto2[1],2))
      else :
        distancia = math.sqrt(math.pow(self.punto2[0]-self.punto1[0],2)+math.pow(self.punto2[1]-self.punto1[1],2))
      return distancia

    def base(self):
        base = 0
        if self.punto1[0]>self.punto2[0]:
            base = self.punto1[0] - self.punto2[0]
        else :
            base = self.punto2[0] - self.punto1[0]
        return base

    def altura(self):
        altura = 0
        if self.punto1[1]>self.punto2[1]:
            altura = self.punto1[1] - self.punto2[1]
        else :
            altura = self.punto2[1] - self.punto1[1]
        return altura

    def area(self):
      return self.base()*self.altura()
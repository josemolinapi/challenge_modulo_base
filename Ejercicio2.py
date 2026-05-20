import math

class punto:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        print(f'({x},{y})')

    def cuadrante(self):
        if self.x>0 and self.y>0:
            print('Cuadrante 1')
        elif self.x<0 and self.y>0:
            print('Cuadrante 2')
        elif self.x<0 and self.y<0:
            print('Cuadrante 3') 
        elif self.x>0 and self.y<0:
            print('Cuadrante 4')
        elif self.x==0 and self.y==0:
            print('Origen')

    def vector(self, punto):
      return (punto.x-self.x,punto.y-self.y)

    def distancia(self, punto):
      vector = self.vector(punto)
      return math.sqrt((vector[0]**2)+(vector[1]**2))
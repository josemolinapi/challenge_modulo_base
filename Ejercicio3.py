class MinionsGame:
    def __init__(self, s):
        self.s = s

    def jugar(self):
        s = self.s
        puntos_kevin = 0
        puntos_stuart = 0
        
        for i,letra in enumerate(s):
            puntos = len(s) - i

            if letra in 'AEIOU':
                puntos_kevin += puntos
            else:
                puntos_stuart += puntos
        return puntos_kevin, puntos_stuart
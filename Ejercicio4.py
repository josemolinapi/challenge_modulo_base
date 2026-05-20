class Vector:
    def __init__(self, weights):
        self.weights = weights

    def set_weights(self, weights):
        self.weights = weights

    def dot(self, x):
        resultado = 0

        for w, v in zip(self.weights, x):
            resultado += w * v

        return resultado

    def predict(self, x):
        resultado = self.dot(x)

        return max(0, resultado)


class Bias(Vector):
    def __init__(self, weights, bias):
        super().__init__(weights)
        self.bias = bias

    def dot(self, x):
        resultado = super().dot(x)

        return resultado + self.bias
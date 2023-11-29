import math

class FiguraGeometrica:
    def calculararea(self):
        pass

    def calcularperimetro(self):
        pass

    def __str__(self):
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calculararea(self):
        return self.base * self.altura

    def calcularperimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Retângulo - Base: {self.base}, Altura: {self.altura}"

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura, lado1, lado2):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calculararea(self):
        return (self.base * self.altura) / 2

    def calcularperimetro(self):
        return self.base + self.lado1 + self.lado2

    def __str__(self):
        return f"Triângulo - Base: {self.base}, Altura: {self.altura}, Lado1: {self.lado1}, Lado2: {self.lado2}"

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calculararea(self):
        return math.pi * (self.raio ** 2)

    def calcularperimetro(self):
        return 2 * math.pi * self.raio

    def __str__(self):
        return f"Círculo - Raio: {self.raio}"

retangulo = Retangulo(9, 6)
triangulo = Triangulo(4, 8, 2, 6)
circulo = Circulo(5)

print(retangulo)
print(f"Área do Retângulo: {retangulo.calculararea()}")
print(f"Perímetro do Retângulo: {retangulo.calcularperimetro()}")
print("\n")
print(triangulo)
print(f"Área do Triângulo: {triangulo.calculararea()}")
print(f"Perímetro do Triângulo: {triangulo.calcularperimetro()}")
print("\n")
print(circulo)
print(f"Área do Círculo: {circulo.calculararea()}")
print(f"Circunferência do Círculo: {circulo.calcularperimetro()}")
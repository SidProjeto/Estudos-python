from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self,lados=1):
        super().__init__(4)
        self.lados = lados

    def perimetro(self):
        peri = self.lados * self.qtd_lados
        return peri

    def area(self):
        area = self.lados ** 2
        return area


class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        peri = 2 * pi * self.raio
        return peri

    def area(self):
        area = pi  * self.raio ** 2
        return area
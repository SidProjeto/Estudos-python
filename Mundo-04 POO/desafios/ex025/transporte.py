from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia, frete):
        self.dist = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, 0.50)

    def calc_frete(self):
        calc = self.dist * self.frete
        return f'R${calc:.2f}'


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, 1.20)

    def calc_frete(self):
        if self.dist < 50:
            return f'Raio mínimo de 50km'
        else:
            calc = self.dist * self.frete
            return f'R${calc:.2f}'



class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, 9.50)

    def calc_frete(self):
        if self.dist > 10:
            return f'Raio máximo de 10km'
        else:
            calc = self.dist * self.frete
            return f'R${calc:.2f}'

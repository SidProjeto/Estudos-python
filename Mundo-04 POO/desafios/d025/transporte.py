from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.dist = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.dist * Moto.fator
        return f'R${self.frete:.2f}'


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.dist < 50:

            self.frete = 0
            return f'Raio mínimo de 50km'
        else:

            self.frete = self.dist * Caminhao.fator
            return f'R${self.frete:.2f}'



class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.dist > 10:

            self.frete = 0
            return f'Raio máximo de 10km'
        else:
            
            self.frete = self.dist * Drone.fator
            return f'R${self.frete:.2f}'

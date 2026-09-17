
class Termostato:
    def __init__(self):
        self.__temperatura = 24
        

    @property
    def ftemperatura(self):
        return f'{self.temperatura}°C'
    
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,valor):
        if valor < 16:
            self.__temperatura = 16

        elif valor > 30:
             self.__temperatura = 30
             
        elif valor % 1 == 0.5 or valor % 1 == 0.0:
                self.__temperatura = valor

        else:
            raise ValueError(f'A temperatura de {valor}°C é invalida!')
from abc import ABC, abstractmethods

class Funcionario(ABC):
    def __init__(self, nome: str = '', salario: int|float = 0):
        self.nome = nome
        self.__salario = salario

    @abstractmethods
    def calcular_bonus(self) -> float:
        pass

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: int|float = 0):

        if not isinstance(salario, (int,float)):
            raise TypeError('O salário dever um valor inteiro ou real')
        
        if salario < 0:
            raise ValueError('Salário não pode ser menor que 0')

        if salario <= self.__salario:
            raise ValueError('você não pode reduzir o salário de um funcionário.')
        
        self.__salario = salario

class Gerente(Funcionario):
    taxa_bonus = 0.15
    
    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)

    def calcular_bonus(self) -> float:
        bonus = self.salario * Gerente.taxa_bonus
        return bonus
    
    def __str__(self):
        return f'{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}'

class Designer(Funcionario):
    taxa_bonus = 0.08

    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)

    def calcular_bonus(self) -> float:
        bonus = self.salario * Designer.taxa_bonus
        return bonus
    
    def __str__(self):
        return f'{self.nome} ganha R${self.salario:.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}'


class Desenvolvedor(Funcionario):
    taxa_bonus = 0.10

    def __init__(self, nome = '', salario = 0):
        super().__init__(nome, salario)

    def calcular_bonus(self) -> float:
        bonus = self.salario * Desenvolvedor.taxa_bonus
        return bonus
    
    def __str__(self):
        return f'{self.nome} ganha R${self.salario:.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}'
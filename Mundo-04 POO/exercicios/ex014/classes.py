from functools import singledispatchmethod

class Analisador:

    @singledispatchmethod
    def analizar(self, valor):
        print(f'Não foi possivel analizar o valor {valor}')

    @analizar.register
    def _(self, valor: int):
        print(f'{valor} é um número inteiro')

    @analizar.register
    def _(self, valor: float):
        print(f'{valor} é um número com ponto flutuante (Real)')

    @analizar.register
    def _(self, valor: bool):
        print(f'{valor} é um valor booleano (verdadeiro ou falso)')

    @analizar.register
    def _(self, valor: str):
        print(f'{valor} é uma cadeia de caracteres')

    @analizar.register
    def _(self, valor: tuple | list | dict):
        print(f'{valor} é uma coleção de dados')
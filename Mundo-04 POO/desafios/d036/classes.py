from abc import ABC, abstractmethod
from locale import LC_ALL, currency, setlocale


class Pagamento(ABC):
    setlocale(LC_ALL, 'pt_BR.UTF-8')

    def __init__(self):
        self._valor = None

    @property
    def fvalor(self):
        return currency(self.valor, grouping=True)
    
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor < 0:
            raise ValueError('O Valor não pode ser abaixo de 0')

        else:
            self._valor = valor

    @abstractmethod
    def pagar(self, valor: float):
        pass


class Boleto(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f'Pagamento CONFIRMADO de {self.fvalor} via Boleto'
        except:
            return f'Falha no pagamento de {self.fvalor} via Boleto'


class Pix(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f'Pagamento CONFIRMADO de {self.fvalor} via Pix'
        except:
            return f'Falha no pagamento de {self.fvalor} via Pix'


class CartaoCredito(Pagamento):
    def pagar(self, valor: float):
        try:
            self.valor = valor
            return f'Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito'
        except:
            return f'Falha no pagamento de {self.fvalor} via Cartão de Crédito'


def finalizar_compra(metodo, valor):
    print(metodo.pagar(valor))
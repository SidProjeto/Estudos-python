from abc import ABC, abstractmethod
from locale import setlocale, currency, LC_ALL



class Pagamento(ABC):
    setlocale(LC_ALL, 'pt_BR.UTF-8')

    def pagar(self, valor):
        print(f'Pagamento CONFIRMADO de {currency(valor, grouping=True)} via {self.__class__.__name__}')


class Boleto(Pagamento):
    def pagar(self, valor):
        print(f'Pagamento CONFIRMADO de {currency(valor, grouping=True)} via Boleto')


class Pix(Pagamento):
    def pagar(self, valor):
        print(f'Pagamento CONFIRMADO de {currency(valor, grouping=True)} via Pix')


class CartaoCredito(Pagamento):
    def pagar(self, valor):
        print(f'Pagamento CONFIRMADO de {currency(valor, grouping=True)} via Cartão de Crédito')


def finalizar_compra(metodo, valor):
    metodo.pagar(valor)
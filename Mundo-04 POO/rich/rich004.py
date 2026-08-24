from rich import print
from rich import inspect


class ContaBancaria:
    """
    Crie uma conta bancária e permite saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de Saldo"

    def sacar(self, valor):
        if valor > self.saldo:
            print(
                f"Saque negado de {valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE"
            )
        else:
            self.saldo -= valor
            return f"Saque de R${valor:,.2f} autorizado na conta {self.id}"

    def depositar(self, valor):
        self.saldo += valor
        return f"Depósito de R${valor:,.2f} autorizado na conta {self.id}"


c = ContaBancaria(112, "Arthur", 3000)
inspect(c)

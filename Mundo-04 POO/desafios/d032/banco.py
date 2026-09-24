from hashlib import sha256
from getpass import getpass

class ContaBancaria:
    def __init__(self, id: int, nome: str, saldo: float, senha: str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        self.__hash = senha

        if not senha:
            senha = self.pede_senha()
        senha = str(senha)
        senha_criptografada = sha256(senha.encode()).hexdigest()
        self.__hash = senha_criptografada

    def pede_senha(self) -> str:
        senha = getpass('Senha: ', echo_char='*').strip()
        return senha

    def validar_senha(self, senha: str) -> bool:
        senha = str(senha)
        senha_criptografada = sha256(senha.encode()).hexdigest()
        if senha_criptografada == self.__hash:
            return True

        else:
            return False

    @property
    def nome(self):
        return self._titular

    @property
    def saldo(self) -> str:
         return f'R${self.__saldo:.2f}'

    @nome.setter
    def nome(self, nome):
        print('Para alterar nome, coloque sua senha')
        senha = self.pede_senha()

        if self.validar_senha(senha):
            self._titular = nome

        else:
            print('Senha incorreta! Nome não alterado')

    def depositar(self, valor: float):
        if valor <= 0:
            print(f'Não é possivel depositar valores abaixo ou igual a 0')

        else:
            self.__saldo += valor
            print('Deposito efetuado com sucesso!')


    def sacar(self, valor: float, senha: str = None):
        if valor <= 0:
            print('Valor invalido! para sacar')

        elif valor <= self.__saldo:

            if not senha:
                print('Para efetuar o saque, coloque sua senha')
                senha = self.pede_senha()

            if self.validar_senha(senha):
                print('Saque efetuado com sucesso!')
                self.__saldo -= valor

            else:
                print('Saque não efetuado! senha incorreta!')

        else:
            print('Saldo insuficiente!')


   

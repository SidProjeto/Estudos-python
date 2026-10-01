from hashlib import sha256
from getpass import getpass

class ContaBancaria:
    def __init__(self, id: int, nome: str = None, saldo: float = 0, senha: str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if not senha:
            senha = self.pede_senha()

        self.__hash = sha256(str(senha).encode()).hexdigest()


    def pede_senha(self) -> str:
        while True:
            msg = ''
            senha = getpass('Senha: ', echo_char='*').strip()
            if len(senha) >= 4:
                break
            else:
                print('Senha tem que ter no mínimo 4 digitos')
                while True:
                    msg = input('deseja continuar ? [S/N]: ').upper().strip()
                    if msg in "SN":
                       break
            if msg == 'N':
                raise PermissionError('Operação cancelada pelo usuário')

        return senha

    def validar_senha(self, senha: str) -> bool:
        senha = sha256(str(senha).encode()).hexdigest()
        if senha == self.__hash:
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
            raise PermissionError('Senha incorreta! Nome não alterado')

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError(f'Não é possivel depositar valores abaixo ou igual a 0')

        else:
            self.__saldo += valor
            print('Deposito efetuado com sucesso!')


    def sacar(self, valor: float, senha: str = None):
        if valor <= 0:
            raise ValueError('Valor invalido! para sacar')

        elif valor <= self.__saldo:

            if not senha:
                print('Para efetuar o saque, coloque sua senha')
                senha = self.pede_senha()
            
            if self.validar_senha(senha):
                print('Saque efetuado com sucesso!')
                self.__saldo -= valor

            else:
                raise PermissionError('Saque não efetuado! senha incorreta!')

        else:
            raise ValueError('Saldo insuficiente!')
        
    def __str__(self):
        return f'A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo'
   

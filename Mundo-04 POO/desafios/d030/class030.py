from hashlib import sha256
from rich import print

class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self,valor):
        if type(valor) != str:
            valor = str(valor)
        senha_criptografada = sha256(valor.encode()).hexdigest()
        self.__hash = senha_criptografada

    def validar(self,chave):
        if type(chave) != str:
            chave = str(chave)
        senha_criptografada = sha256(chave.encode()).hexdigest()
        if senha_criptografada == self.__hash:
            return 'Senha Confere!\n[green]True[/]'
        else:
            return'Senha não bate!\n[red]False[/]'

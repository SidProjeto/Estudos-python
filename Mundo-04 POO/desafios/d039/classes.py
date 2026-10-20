from abc import ABC, abstractmethod
from re import match


class Validador(ABC):

    @abstractmethod
    def validar(self, valor):
        pass


class Usuario(Validador):

    def validar(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome de Usuário deve ser uma string")

        if not match(r"^[a-z0-9_]{5,20}$", valor):
            raise ValueError('Usuario Invalido!')

        return True


class Email(Validador):
    def validar(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O email deve ser uma string")

        if not match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$", valor):
            raise ValueError('Email Invalido!')

        return True

class Senha(Validador):

    def validar(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A senha deve ser uma string")

        if not match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$', valor):
            raise ValueError('Senha Invalida!')

        return True

def validar_dado(validador, valor):
    vali = None
    motivo = None
    try:
        validador.validar(valor)
        vali = 'SIM'

    except Exception as e:
        vali = 'NÃO'
        motivo = e

    print(f'Valor: {valor} é valido: {vali}')
    if motivo:
        print(f'Motivo: {motivo}')



    

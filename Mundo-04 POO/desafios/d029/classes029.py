from rich import print

class Diario:
    def __init__(self, senha=1234):
        self.__segredos = []
        self.__senha = senha


    @property
    def senha(self):
        raise PermissionError(f'Ninguém tem permissão de ver a senha')
    
    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha=None):
        if senha == self.__senha:
            print('[green]Diario LIBERADO!')
            for linha in self.__segredos:
                print(f'- {linha}', end='\n')
        else:
            raise PermissionError(f'Você não tem permissão para ler o meu diario!')
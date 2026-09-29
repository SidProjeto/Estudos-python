class Diario:
    def __init__(self, senha=1234):
        self.__segredos = []
        self.__senha = str(senha).strip()


    @property
    def senha(self):
        raise PermissionError(f'Ninguém tem permissão de ver a senha')

    @senha.setter
    def senha(self, senhas=('','')):
        senha, nova_senha = str(senhas[0]).strip(), str(senhas[1]).strip()
        if senha == self.__senha:
            if nova_senha != senha:
                self.__senha = nova_senha
            else:
                raise ValueError('A nova senha não pode ser igual a anterior!')
        else:
            raise ValueError('Senha incorreta!')
    
    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha=None):
        if senha:
            senha = str(senha).strip()
        if senha == self.__senha:
            print('[green]Diario LIBERADO!')
            for linha in self.__segredos:
                print(f'- {linha}', end='\n')
        else:
            raise PermissionError(f'Você não tem permissão para ler o meu diario!')
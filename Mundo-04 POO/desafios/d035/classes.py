from abc import ABC, abstractmethod

class Arquivo(ABC):
    mb = 1000000
    def __init__(self, nome, tamanho, extensao=''):
        self.nome = nome
        self.extensao = extensao
        if tamanho <= 0:
            raise ValueError('O tamanho do arquivo não pode ser menor que 1')

        else:
            self.tamanho = f'{(tamanho / Arquivo.mb):.2f}MB'

    @property
    def nome_completo(self):
        return f"'{self.nome}{self.extensao}' ({self.tamanho})"


    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, extensao='.pdf')

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

class DOC(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho, extensao='.doc')

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")


def abrir_arquivo(objeto):
    try:
        objeto.abrir()
    except:
        print(f'Ocorreu um erro ao tentar abrir o objeto do tipo {objeto.__class__.__name__}')
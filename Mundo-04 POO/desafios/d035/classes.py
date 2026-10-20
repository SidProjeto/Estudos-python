from abc import ABC, abstractmethod


class Arquivo(ABC):
    def __init__(self, nome: str, tamanho: int, ext: str):
        self.nome = nome
        self.extensao = ext
        if tamanho <= 0:
            raise ValueError("O tamanho do arquivo não pode ser menor que 1")

        else:
            self.tamanho = tamanho

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}' ({(self.tamanho / 1_000_000)}MB)"

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext: str):
        ext = ext.lower().strip()

        if ext == "pdf" or ext == "doc" or ext == 'docx':
            self._extensao = ext

        else:
            raise AttributeError(f"A extensão '{ext}' não é suportada")

    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    def __init__(self, nome: str, tamanho: int):
        super().__init__(nome, tamanho, ext="pdf")

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")


class DOC(Arquivo):
    def __init__(self, nome: str, tamanho: int):
        super().__init__(nome, tamanho, ext="docx")

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")


def abrir_arquivo(objeto):
    try:
        objeto.abrir()

    except Exception as e:
        print(f"Ocorreu um erro ao tentar abrir o objeto do tipo {objeto.__class__.__name__}")
        print(f"detalhes do erro: {e}")

from rich import print
from rich.traceback import install

install()


class Funcionario:
    def __init__(
        self,
        nome="vazio",
        setor="desconhecido",
        cargo="desconhecido",
        empresa="Curso em Video",
    ):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentar(self) -> str:
        return f":handshake:[bold] Olá, sou [cyan]{self.nome}[/] e sou [cyan]{self.cargo}[/] do setor de [cyan]{self.setor}[/] da [cyan]{self.empresa}[/][/]"


f1 = Funcionario("Maria", "Administração", "Diretora")
print(f1.apresentar())

f2 = Funcionario("Pedro", "TI", "Programador")
print(f2.apresentar())

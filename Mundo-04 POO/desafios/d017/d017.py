from rich import print
from rich.traceback import install
from rich.panel import Panel

install()


class Produto:
    def __init__(self, nome="NULL", preco=0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += "-" * 30
        precoformat = f"R${self.preco:,.2f}"
        conteudo += f"{precoformat.center(30, '.')}"
        painel = Panel(conteudo, title="Produto", width=34)

        return painel

    def __str__(self):
        return f"{self.nome} custa R${self.preco:,.2f}"


p1 = Produto("Iphone 17 Pro Max", 2_5000.85)
print(p1.etiqueta())
p2 = Produto("Notebook Gamer", 8_000)
print(p2.etiqueta())

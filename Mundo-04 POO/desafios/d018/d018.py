from rich import print
from rich.traceback import install
from rich.panel import Panel

install()


class Churrasco:
    preco = 82.40
    comsumo_padrao = 0.400  # g por pessoa

    def __init__(self, titulo, pessoas):
        self.nome = titulo
        self.qtdepessoas = pessoas

    def calcular_qtd_carne(self):
        return self.qtdepessoas * Churrasco.comsumo_padrao

    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * Churrasco.preco

    def calcular_custo_individual(self):
        return self.calcular_custo_total() / self.qtdepessoas

    def analisar(self):
        conteudo = f"Analisando [green]{self.nome}[/] com [blue]{self.qtdepessoas} convidados[/]\n"
        conteudo += f"Cada participante comerá [blue]{Churrasco.comsumo_padrao:.1f}kg[/] e cada kg custa [red]R${self.preco:,.2f}[/]\n"
        conteudo += (
            f"Recomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne\n"
        )
        conteudo += (
            f"O Custo Total será de [red]R${self.calcular_custo_total():,.2f}[/]\n"
        )
        conteudo += f"Cada pessoa pagará [red]R${self.calcular_custo_individual():,.2f}[/] para participar."
        caixa = Panel(
            conteudo,
            title=self.nome,
            width=70,
        )
        print(caixa)
    def __str__(self):
        return f'Nome do churrasco é {self.nome} e quantidade pessoas é {self.qtdepessoas}'


g1 = Churrasco("Churras dos Amigos", 15)
g1.analisar()
g2 = Churrasco("Festa do fim de ano", 80)
g2.analisar()

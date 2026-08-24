from rich import print


class Caneta:
    def __init__(self, cor):
        self.cor_caneta = cor
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def quebra_linha(self, qtd):
        if self.tampada:
            print("Destampe a caneta primeiro!")
        else:
            for c in range(qtd + 1):
                print("\n", end="")

    def escrever(self, msg):
        if self.tampada:
            print("Destampe a caneta primeiro!")
        else:
            cor = self.cor_caneta.lower()
            cores = {
                "limpar": "[/]",
                "preto": "[black]",
                "vermelho": "[red]",
                "verde": "[green]",
                "amarelo": "[yellow]",
                "azul": "[blue]",
                "roxo": "[magenta]",
                "ciano": "[cyan]",
                "branco": "[white]",
            }
            print(f"{cores[cor]}{msg}[/]", end=" ")


c1 = Caneta("ciano")
c2 = Caneta("vermelho")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem?")
c1.quebra_linha(2)
c2.escrever("Olá, Gafanhoto!")
c3.escrever("Vamos exercitar!")

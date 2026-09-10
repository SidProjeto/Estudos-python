from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    inss = 7.5
    salario_min = 1612
    def __init__(self, nome=None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0


    def analisar_salario(self):
        base = self.salario / Funcionario.salario_min
        msg = f"O salario de [cyan]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{base:.1f} salários mínimos[/]."

        panel = Panel(msg, title="Análise de Salário",width=50,)
        print(panel)

    @abstractmethod
    def calc_salario(self):
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora=7.37, horas_tab=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_tab = horas_tab
        self.sal_bruto = self.valor_hora * self.horas_tab

    def calc_salario(self):
        self.salario = self.sal_bruto - ( self.sal_bruto * (Funcionario.inss / 100))
        return self.salario


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto=Funcionario.salario_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto
    def calc_salario(self):
        self.salario = self.sal_bruto - ( self.sal_bruto * (Funcionario.inss / 100))
        return self.salario

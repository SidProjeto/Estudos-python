from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome, sal_bruto, salario):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5

    def analisar_cal(self):
        panel = Panel(
            f"O salario de [cyan]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.calc_sal():.2f}[/] e corresponde a [yellow]{(self.calc_sal() / self.sal_min):.1f} salários mínimos[/].",
            title="Análise de Salário",
            width=50,
        )
        print(panel)

    @abstractmethod
    def calc_sal(self):
        pass


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_tab):
        super().__init__(nome, sal_bruto=None, salario=None)
        self.valor_hora = valor_hora
        self.horas_tab = horas_tab

    def calc_sal(self):
        salario = (self.valor_hora * self.horas_tab)
        salario_final = salario - ( salario * (self.inss / 100))
        return salario_final


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto, salario=None)

    def calc_sal(self):
        salario_final = self.sal_bruto - ( self.sal_bruto * (self.inss / 100))
        return salario_final

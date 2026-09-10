from salario import *
from rich import inspect


def main():
    f1 = FuncionarioHorista("Paulo", 25, 250)
    f1.calc_salario()
    f1.analisar_salario()
    # inspect(f1)

    f2 = FuncionarioMensalista("Amanda", 8500)
    f2.calc_salario()
    f2.analisar_salario()
    # inspect(f2)


if __name__ == "__main__":
    main()

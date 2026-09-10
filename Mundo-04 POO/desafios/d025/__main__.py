from transporte import *
from rich import print
from rich.table import Table


def tabela_fretes(dist):
    transportes = [Moto(dist), Caminhao(dist), Drone(dist)]

    tab = Table(title="Tabela de Fretes")
    tab.add_column("Distância")
    tab.add_column("Tipo")
    tab.add_column("Frete")

    for veiculo in transportes:
        tab.add_row(f"{dist}km", type(veiculo).__name__, veiculo.calc_frete())
        
    print(tab)


def main():
    dist = 93
    tabela_fretes(dist)


if __name__ == "__main__":
    main()

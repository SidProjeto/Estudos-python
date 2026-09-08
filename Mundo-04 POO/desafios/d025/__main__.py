from transporte import *
from rich import print
from rich.table import Table


def tabela(dist):
    moto = Moto(dist)
    caminhao = Caminhao(dist)
    drone = Drone(dist)
    tab = Table()
    tab.add_column("Distância")
    tab.add_column("Tipo")
    tab.add_column("Frete")

    tab.add_row(f"{dist}km", type(moto).__name__, moto.calc_frete())
    tab.add_row(f"{dist}km", type(caminhao).__name__, caminhao.calc_frete())
    tab.add_row(f"{dist}km", type(drone).__name__, drone.calc_frete())
    print(tab)


def main():
    dist = 100
    tabela(dist)


if __name__ == "__main__":
    main()

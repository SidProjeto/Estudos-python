from transporte import *
from rich import print


def main():
    dist = 8

    entrega = Drone(dist)
    print(f"Frete do {type(entrega).__name__} em {dist}Km = {entrega.calc_frete()}")


if __name__ == "__main__":
    main()

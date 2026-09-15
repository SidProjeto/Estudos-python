from rpg import *
from rich import inspect


def main():
    p1 = Guerreiro("Megaman", 1000)
    p2 = Mago("Merlin", 5000)
    p3 = Guerreiro("Kratos", 1500)
    p1.atacar(p2, 100)
    p3.atacar(p1, 100)
    p2.atacar(p3, 100)

    p1.status()
    p2.status()
    p3.status()


if __name__ == "__main__":
    main()

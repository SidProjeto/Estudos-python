from rpg import *


def main():
    p = Guerreiro("guer", 200)
    p2 = Mago("mag", 200)
    p.atacar(p2, 200)
    p2.atacar(p, 200)
    p.curar()
    p2.curar()
    p.atacar(p2, 200)
    p2.atacar(p, 200)

if __name__ == "__main__":
    main()

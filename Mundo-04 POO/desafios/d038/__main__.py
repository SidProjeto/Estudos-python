from classes import *


def main():
    p1 = Produto("caderno", 32.62)
    p2 = Produto("Caneta", 8.50)
    p3 = Produto("Mochila", 430.44)
    p4 = Produto("Estojo", 85.38)
    c1 = Carrinho()
    c2 = Carrinho()
    c1 = c1 + p1 + p2 + p4
    c2 += c1
    print(c1)
    print(c2)


if __name__ == "__main__":
    main()

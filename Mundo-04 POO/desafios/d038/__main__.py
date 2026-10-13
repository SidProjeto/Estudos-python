from classes import *


def main():
    p1 = Produto("Mouse", 325)
    p2 = Produto("Memória 256gb", 1800)
    p3 = Produto("Placa de video", 25999)
    p4 = Produto("Teclado", 433)
    c1 = Carrinho()
    c2 = Carrinho()
    c3 = Carrinho()
    c1 = c1 + p1 + p2
    c2 = c2 + p3 + p4
    c3 = c1 + c2
    print(c1)


if __name__ == "__main__":
    main()

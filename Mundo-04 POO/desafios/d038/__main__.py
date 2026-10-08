from classes import *


def main():
    p1 = Produto("Mouse", 325)
    p2 = Produto("Memória 256gb", 1800)
    p3 = Produto("Placa de video", 25999)
    p4 = Produto('Teclado', 433)
    c1 = Carrinho()
    c2 = Carrinho()
    c1 = c1 + p1 + p2 + p3

    c2 = c2 + c1 + p4
    print(c2)


if __name__ == "__main__":
    main()

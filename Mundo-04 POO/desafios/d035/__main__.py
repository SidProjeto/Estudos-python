from classes import *
from rich import inspect, print


def main():
    a1 = DOC("prova", 550_000)
    a2 = PDF("contrato", 1_200_000)

    abrir_arquivo(a1)
    abrir_arquivo(a2)
    print(a2.nome_completo)
    print(a1.nome_completo)
    inspect(a1, private=True, methods=True)


if __name__ == "__main__":
    main()

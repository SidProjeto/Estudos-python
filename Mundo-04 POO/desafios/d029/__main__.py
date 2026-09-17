from classes029 import Diario
from rich import inspect


def main():
    d = Diario("1234")
    d.escrever(f"Primeira mensagem")
    d.escrever(f"Você é uma pessoa simpática")
    d.escrever(f"Você gosta de Python")

    d.ler("1234")
    inspect(d, private=True, methods=True)


if __name__ == "__main__":
    main()

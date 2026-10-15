from classes import *


def main():
    funcionarios = [
        Desenvolvedor("Pedro", 18_000),
        Designer("José", 25_000),
        Gerente("Mariana", 45_0000),
    ]

    for func in funcionarios:
        print(func)


if __name__ == "__main__":
    main()

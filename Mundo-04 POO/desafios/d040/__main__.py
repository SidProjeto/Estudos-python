from classes import *


def main():
    u = [
        Usuario("Pedro", "pedro@gmail.com"),
        Usuario("Maria", "mariazinha@hotmail.com"),
    ]

    a = [
        Aluno("Claudia", "ADS", "2 per"),
        Aluno("Ana", "ADM", "4 per"),
        Aluno("Mario", "SEG", "1 per"),
    ]

    exportar_dados(XML(), a)


if __name__ == "__main__":
    main()

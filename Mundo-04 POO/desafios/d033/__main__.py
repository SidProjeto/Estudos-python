from rich import print, inspect
from alunos import *


def main():
    a = Aluno("Maria", 2002, "ads")
    a.adicionar_curso("moda")
    a.curso = "moda"

    inspect(a, private=True, methods=True)


if __name__ == "__main__":
    main()

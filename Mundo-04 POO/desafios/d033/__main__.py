from rich import print, inspect
from alunos import *


def main():
    a = Aluno("Maria", 2002, "kkk")
    a.curso = "kkk"

    inspect(a, private=True, methods=True)


if __name__ == "__main__":
    main()

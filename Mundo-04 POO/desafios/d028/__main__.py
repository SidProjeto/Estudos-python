from classes028 import *
from rich import inspect


def main():
    t = Termostato()
    t.temperatura = 25.5
    inspect(t, private=True, methods=True)
    print(f"A temperatura atual é {t.ftemperatura}")


if __name__ == "__main__":
    main()

from classes028 import *
from rich import inspect


def main():
    t = Termostato()
    try:
        t.temperatura = 25.5
        
    except Exception as e:
        print(f'Houve um problema: {e}')
        
    print(f"A temperatura atual é {t.ftemperatura}")
    inspect(t, private=True, methods=True)

if __name__ == "__main__":
    main()

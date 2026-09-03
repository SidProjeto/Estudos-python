from poligono import *
from rich import print, inspect

def main():
    p1 = Circulo(20)

    print(f"O perímetro = {p1.perimetro():.1f}")
    print(f"Area = {p1.area():.1f}")


if __name__ == "__main__":
    main()

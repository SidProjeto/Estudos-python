from poligono import *
from rich import print, inspect


def main():
    p1 = Quadrado(20)
    # inspect(p1, methods=True)
    print(f"O quadrado de lado {p1.lados}m tem perímetro = {p1.perimetro():.1f}m")
    print(f"O quadrado de lado {p1.lados}m tem Area = {p1.area():.1f}m²")

    p2 = Circulo(12)
    # inspect(p2, methods=True)
    print(f"Um circulo de raio {p2.raio}m tem perímetro = {p2.perimetro():.1f}m")
    print(f"Um circulo de raio {p2.raio}m tem area = {p2.area():.1f}m²")


if __name__ == "__main__":
    main()

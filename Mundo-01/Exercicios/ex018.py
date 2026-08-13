from math import cos, sin, tan, radians
print('Calculador de seno,cosseno e tangente')
n = float(input('Qual o ângulo: '))
r = radians(n)
cos = cos(r)
sin = sin(r)
tan = tan(r)
print(f'Cosseno é {cos:.2f}\nSeno é {sin:.2f}\nTangente é {tan:.2f}')

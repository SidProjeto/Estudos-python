print('\033[1;33mFormador de triângulos e sua forma\033[0m')
com1 = float(input('Primeiro comprimeto: '))
com2 = float(input('Segundo comprimento: '))
com3 = float(input('Terceiro comprimento: '))
if com1 + com2 > com3 and com2 + com3 > com1 and com1 + com3 > com2:
    print('\033[1;32mForma um Triângulo\033[0m')
    if com1 == com2 == com3:
        print('Sua forma é EQUILÁTERO')
    elif com1 == com2 != com3 or com2 == com3 != com1 or com1 == com3 != com2:
        print('Sua forma é  ISÓSCELES')
    elif com1 != com2 != com3 or com2 != com3 != com1 or com1 != com3 != com2:
        print('Sua forma é ESCALENO')
else:
    print('\033[1;31mNão forma um Triângulo\033[0m')
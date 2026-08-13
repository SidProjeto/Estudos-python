print('\033[1;33m','='*5,'Calculador de Nota','='*5,'\033[0m')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota : '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'Você tirou {media:.2f} e foi \033[1;32mAPROVADO\033[0m')
elif media >= 5 and media < 7:
    print(f'Você tirou {media:.2f} e ficou de \033[1;37mRECUPERAÇÃO\033[0m')
elif media < 5:
    print(f'Você tirou {media:.2f} e foi \033[1;31mREPROVADO\033[0m')
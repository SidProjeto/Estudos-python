numeros = ('Zero', 'Um','Dois','Três','Quatro','Cinco',
           'Seis','Sete','Oito','Nove','Dez',
           'Onze','Doze','Treze','Cartoze','Quinze',
           'Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.',end=' ')
    print(f'Você digitou o número {numeros[num]}')
    continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()
    if continuar not in 'S':
        break
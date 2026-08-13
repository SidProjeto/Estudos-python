frase = str(input('Digite a frase: ')).strip().lower().replace(' ','')
pali = frase == frase[::-1]
if pali == True:
    print('é um palíndromo')
else:
    print('não é um palíndromo')
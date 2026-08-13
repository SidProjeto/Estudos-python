frase = str(input('Digite a frase: ')).strip()
print(f'A letra "a" pareceu: {frase.upper().count('A')}')
print(f'A letra "a" apareceu pela primeira vez: {frase.upper().find('A') + 1}')
print(f'A letra "a" apareceu por ultimo: {frase.upper().rfind('A') +1}')
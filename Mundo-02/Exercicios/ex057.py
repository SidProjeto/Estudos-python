n = str(input('Qual seu sexo? [M/F] ')).strip()
while n not in 'MmFf':
    if n != 'M' and n != 'F':
        n = str(input('Dado Invalido! Informe seu Sexo! '))
print(f'Sexo {n} Registrado com sucesso!')
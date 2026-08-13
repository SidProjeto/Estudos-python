palavras = ("Computador","Caneta","Caderno","Mesa","Teclado",
            "Livro","Celular","Garrafa", "Mochila")
cont = 0
while cont != len(palavras):
    print(f'Na palavra {palavras[cont].upper()} temos: ',end='')
    for letras in palavras[cont]:
        if letras in 'aeiou':
            print(letras,end=' ')
    print('')
    cont += 1
from datetime import date
print('Descubra se o ano é bissexto!')
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é Bissexto')
else:
    print(f'{ano} não é bissexto')
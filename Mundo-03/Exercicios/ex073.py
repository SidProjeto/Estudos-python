from time import sleep
tabela = ('Palmeiras','Flamengo','Fluminense','São Paulo','Athletico-PR',
          'Bahia','Red Bull Bragantino','Vasco da Gama','Coritiba','Vitória',
          'Cruzeiro','Botafogo','Atlético-MG','Internacional','Santos',
          'Corinthians','Grêmio','Mirassol','Remo','Chapecoense')
print(f'''{'='*98}
lista de times do Brasileirão: {tabela}
{'='*98}''')
print(f'{'='*5} O G5 do Brasileirão {'='*5}')
for times in tabela[0:5]:
    print(times)
    sleep(0.5)

print(f'{'='*5} O Z4 do brasileirão {'='*5}')
for times in tabela[16:]:
        print(times)
        sleep(0.5)

print(f'{'='*10} Por ordem alfabetica {'='*10}')
for times in sorted(tabela):
    print(times)
    sleep(0.5)
    
print(f'''{'='*30}
Chapecoense está na {tabela.index('Chapecoense') + 1}º posição''')
estado = dict()
brasil = list()
for c in range(3):
    estado['utf'] = str(input('Unidade Federativa '))
    estado['sigla'] = str(input('Sigla do Estado '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v,end= ' ')
    print()

'''brasil = []
estado = {'uf': 'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf': 'São Paulo','sigla':'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil[1]['sigla'])'''

'''pessoas = {'nome':'Gustavo','sexo':'M','idade':22}
pessoas['peso'] = 98.5
for k,v in pessoas.items():
    print(f'{k} = {v}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''

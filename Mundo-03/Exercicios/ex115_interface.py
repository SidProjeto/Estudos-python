def linha(tam):
    return "-" * tam
    
def cabecalho(msg, cor='sem',tamanho=0):
    tam = 0
    if tamanho != 0:
        tam = tamanho
    else:
        tam = len(msg) + 4
    print(f"""{cores(cor)}{linha(tam)}
{msg:^{tam}}
{(linha(tam))}{cores()}""")


def cores(estilo='sem'):
    estilo_limpo = estilo.strip().lower()
    tabela_cores = {'sem': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m',
                    'amarelo': '\033[1;33m', 'azul': '\033[1;34m', 'roxo': '\033[1;35m', 
                    'ciano': '\033[1;36m', 'branco': '\033[1;37m'}
    
    return tabela_cores[estilo_limpo]
    
 
def menu(lista):
    c = 1
    for opcao in lista:
        print(f"{cores('branco')}[ {c} ] {opcao}{cores()}")
        c += 1
from rich import print

color = {
    'orange': '\033[38;2;255;95;0m',
    'blue': '\033[38;2;0;135;255m',
    'limpo': '\033[0m'
}

def menu():
    print(f'''
[dodger_blue1]{'=' * 30}[/]
[orange_red1]{'SISTEMA DE CADASTRO'.center(30)}[/]
[dodger_blue1]{'=' * 30}[/]
[dodger_blue1][ [orange_red1]1[/] ][/] - Cadastrar pessoa
[dodger_blue1][ [orange_red1]2[/] ][/] - Listar pessoas
[dodger_blue1][ [orange_red1]3[/] ][/] - Atualizar pessoa
[dodger_blue1][ [orange_red1]4[/] ][/] - Excluir pessoa
[dodger_blue1][ [orange_red1]5[/] ][/] - Busca por nome
[dodger_blue1][ [orange_red1]0[/] ][/] - Sair
[dodger_blue1]{'=' * 30}[/]''')
    resp = str(input(f'{color["orange"]}Escolha uma opção: {color['limpo']}'))
    return resp

def menu_cadastro():
    print(f'''
[dodger_blue1]{'=' * 26}[/]
[orange_red1]{'NOVO CADASTRO DE PESSOA'.center(26)}[/]
[dodger_blue1]{'=' * 26}[/]''')

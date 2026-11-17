import sqlite3

from rich import print
from sistema import *

nome_banco = 'cadastro.db'
def criar_banco() -> bool:
    try:
        with sqlite3.connect(nome_banco) as db:
            cur = db.cursor()
            cur.execute('''
            CREATE TABLE IF NOT EXISTS pessoas (
            cod INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            altura REAL NOT NULL
            );
            ''')
            return True
    except sqlite3.Error as erro: 
        print(f'[red]Falha na criação do banco: {erro}[/]')
        return False

def cadastro_em_massa():
    cad_pessoas = [
        ("1", "Gustavo", "1.84"),
        ('2', 'Gabriela', '1.63'),
        ('3', 'Pedro', '2.02'),
        ('4', 'Mariana', '1.72'),
    ]

    try:
        with sqlite3.connect(nome_banco) as db:
            cur = db.cursor()
            cur.executemany('''
            INSERT INTO pessoas
            (cod, nome, altura)
            VALUES
            (?, ?, ?)
            ''', cad_pessoas)

    except sqlite3.Error as erro:
        print('[red][ERRO] Falha ao fazer cadastro em massa[/]')


def cadastrar_pessoa() -> bool:
    menu_cadastro()

    #Leitura e Validação dos dados
    val_nome = input(f'{color['orange']}Nome: {color['limpo']}').strip()
    if not val_nome:
        print('[red][ERRO] O nome é um campo obrigatório![/]')
        return False

    val_altura = input(f'{color['orange']}Altura (metros): {color['limpo']}').strip().replace(',','.')
    if not val_altura:
        print('[red][ERRO] A altura é um campo obrigatório![/]')
        return False

    try:
        altura = float(val_altura)
        if altura <= 0.30 or altura > 3.6:
            print('[red][ERRO] Valor incoerente para altura![/]')
            return False

    except ValueError:
        print('[red][ERRO] A altura precisa ser um número.[/]')
        return False

    try:
        with sqlite3.connect(nome_banco) as db:
            cur = db.cursor()
            cur.execute('''
            INSERT INTO pessoas
            (nome, altura)
            VALUES
            (?, ?)
            ''', (val_nome, val_altura))
            print(f'[green]Cadastro de [bold white]{val_nome}[/] realizado com sucesso![/]')
            return True
    except sqlite3.Error as erro:
        print(f'[red][ERRO] Falha no cadastro no banco: {erro}[/]')
        return False

def listar_pessoa() -> bool:
    pass

def atualizar_pessoa() -> bool:
    pass

def excluir_pessoa() -> bool:
    pass

def buscar_pessoa_por_nome() -> bool:
    pass
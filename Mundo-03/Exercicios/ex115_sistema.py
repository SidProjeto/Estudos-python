import os
from uteis.numeros import *
from ex115_interface import *

def cadastro_pessoa(nome_arquivo):
    """
    -> Realiza o cadastro de uma nova pessoa e armazena os dados em um arquivo de texto.
    :param nome_arquivo: Nome ou caminho do arquivo txt onde os dados serão salvos.
    :return: Não retorna valor (escreve o resultado diretamente no arquivo).
    """
    dados = {}

    cabecalho('CADASTRAR PESSOA', 'amarelo')
    while True:
        try:
            dados["nome"] = str(input("NOME: ")).capitalize()
            break
        except KeyboardInterrupt:
            print('\033[1;33mO usuário encerrou sem informar o campo\033[m')
            dados['nome'] = 'Não informado'
            break
            
    
    dados["idade"] = leiaint("IDADE: ")
            
    print(f"{dados['nome']} foi cadastrado(a) com sucesso")
        
    with open(f"{nome_arquivo}", "a", encoding="utf-8") as f:
        f.write(f"{dados['nome']};{dados['idade']}\n")


def listar_pessoas(arquivo_txt):
    """
    -> Lê os dados de um arquivo de texto e exibe uma listagem formatada de pessoas e idades.
    :param arquivo_txt: Nome ou caminho do arquivo txt a ser lido e listado.
    :return: Não retorna valor (faz apenas a exibição formatada no terminal).
    """
    pessoas = []

    if not os.path.exists(arquivo_txt):
        print("\033[1;31mERRO: Arquivo não existe, cadastre primeiro!\033[m")
        return

    elif os.path.getsize(arquivo_txt) == 0:
        print(f"\033[1;33mAviso: Arquivo está vazio! Cadastre uma pessoa.\033[m")
        return

    with open(f"{arquivo_txt}", "r", encoding="utf-8") as f:
        dados = f.read().splitlines()
    for linha in dados:
        dado = {}
        pessoa = linha.split(";")
        dado["nome"] = pessoa[0]
        dado["idade"] = pessoa[1]
        pessoas.append(dado)

    largura = maior_nome(pessoas)
    cabecalho('LISTAGEM DE PESSOA','amarelo',largura + 20)
    print(f"{'Nome':<{largura}}\t{'Idade':<3}")
    for pessoa in pessoas:
        print(f"{pessoa['nome']:<{largura}}\t{pessoa['idade']:^4} anos")


def maior_nome(lista):
    """
    -> Analisa uma lista de dicionários e descobre o comprimento do maior nome cadastrado.
    :param lista: Lista contendo os dicionários de dados das pessoas (gerada em listar_pessoas).
    :return: Inteiro representando a quantidade de caracteres do maior nome encontrado.
    """
    maior = 0
    for pessoa in lista:
        if maior < len(pessoa["nome"]):
            maior = len(pessoa["nome"])
    return maior

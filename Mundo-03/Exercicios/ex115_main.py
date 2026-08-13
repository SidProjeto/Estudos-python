from ex115_sistema import *
from ex115_sistema import *
from os import system
from time import sleep

nome_arquivo = "cadastros.txt"

while True:
    cabecalho("MENU PRINCIPAL", "amarelo", 30)
    menu(["Cadastrar pessoa", "listar pessoas", "sair"])
    print("\033[1;33m", linha(30), "\033[m")
    resp = str(input("Digite sua opção: ")).strip()

    if resp == "1":
        system("cls" if os.name == "nt" else "clear")
        cadastro_pessoa(nome_arquivo)
        sleep(1)
    elif resp == "2":
        system("cls" if os.name == "nt" else "clear")
        listar_pessoas(nome_arquivo)
        sleep(1)
    elif resp == "3":
        system("cls" if os.name == "nt" else "clear")
        print("<< VOLTE SEMPRE >>")
        break
    else:
        print("\033[1;31mERRO: Opção Invalida!\033[m")
        sleep(1)

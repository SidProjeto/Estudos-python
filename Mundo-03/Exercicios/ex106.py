def pyhelp(comando=""):
    """
    -> Executa um sistema de ajuda que exibe o manual do Python para funções ou bibliotecas.
    :param com: Nome (string) ou objeto da função/biblioteca a consultar (opcional).
    :return: Não retorna valor (execução contínua via terminal no modo interativo).
    """
    
    # Não interativa
    if comando:

        if hasattr(comando, "__name__"):
            comando_str = comando.__name__

        else:
            comando_str = comando

        titulo("Acessando o manual do comando", cores["azul"], comando_str)

        print(cores["verde"])
        help(comando)
        print(cores["reset"])
    #Interativa 
    else:
        while True:
            titulo("SISTEMA DE AJUDA PYHELP", cores["magenta"])

            info = str(input("Função ou Biblioteca > ")).strip()
            if info.lower() == "fim":

                titulo("ATÉ LOGO", cores["vermelho"])

                break

            titulo("Acessando o manual do comando", cores["azul"], info)

            print(cores["verde"])
            help(info)
            print(cores["reset"])


def titulo(msg, cor, comando=""):
    """
    -> Cria e exibe um cabeçalho personalizado e estilizado com linhas adaptáveis.
    :param msg: A mensagem principal que será exibida no centro do título.
    :param cor: O código ANSI da cor que será aplicada ao título.
    :param command: Parâmetro adicional para exibir o nome de um comando específico (opcional).
    :return: Não retorna valor (faz apenas a exibição na tela).
    """
    
    texto = msg

    if comando:
        texto += f" '{comando}'"
    tam = len(texto) + 4
    print(f"""{cor}{"~"*tam}
{texto:^{tam}}
{"~"*tam}\033[0m""")


cores = {
    "preto": "\033[1;30m",
    "vermelho": "\033[1;31m",
    "verde": "\033[1;32m",
    "amarelo": "\033[1;33m",
    "azul": "\033[1;34m",
    "magenta": "\033[1;35m",
    "ciano": "\033[1;36m",
    "branco": "\033[1;37m",
    "reset": "\033[0m",
}

# programa principal
pyhelp(input)
pyhelp()

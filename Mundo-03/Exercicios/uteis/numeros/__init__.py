
def leiaint(msg):
    """
    -> Lê uma string do teclado e valida para aceitar apenas números inteiros.
    :param msg: A mensagem que será exibida no input para o usuário.
    :return: Retorna o número inteiro válido digitado ou 0 em caso de interrupção.
    """
    while True:
        try:
            valor = int(input(msg))
            return valor

        except (ValueError, TypeError):
            print("\033[1;31mERRO: Coloque um valor inteiro válido!\033[m")

        except KeyboardInterrupt:
            print("\n\033[1;33mO Usuário encerrou sem informar os dados!\033[m")
            return 0


def leiafloat(msg):
    """
    -> Lê uma string do teclado e valida para aceitar apenas números reais (float).
    :param msg: A mensagem que será exibida no input para o usuário.
    :return: Retorna o número real válido digitado ou 0 em caso de interrupção.
    """
    while True:

        try:

            valor = str(input(msg)).replace(",", ".")
            return float(valor)

        except (ValueError, TypeError):
            print("\033[1;31mERRO: Coloque um valor real válido!\033[m")

        except KeyboardInterrupt:
            print("\n\033[1;33mO Usuário encerrou sem informar os dados!\033[m")
            return float(0)


def leiadinheiro(dinheiro):
    while True:
        valor = str(input(f"{dinheiro}")).replace(",", ".").strip()
        if not valor.isalpha() and valor != "":
            return float(valor)

        else:
            print(f"\033[1;31mERRO: '{valor}' é um preço inválido!\033[0m")
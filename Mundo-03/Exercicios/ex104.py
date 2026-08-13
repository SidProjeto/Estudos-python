def leiaint(v):
    """
    -> Valida a entrada de dados para garantir que apenas números inteiros sejam aceitos.
    :param v: A mensagem que será exibida na tela durante o input.
    :return: O número inteiro digitado pelo usuário (retornado int).
    """
    print("-" * 30)
    while True:
        n = input(v)
        if n.isnumeric():
            n = int(n)
            return n
        else:
            print("\033[1;31mERRO! Digite um número inteiro válido\033[0m")


# programa Principal
n = leiaint("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
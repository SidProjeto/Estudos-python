def aumentar(n, aumento, show=False):
    """
    -> Calcula o aumento de um determinado preço, retornando o valor com ou sem formatação.
    :param n: O valor numérico inicial a ser calculado.
    :param aumento: A porcentagem de aumento (ex: 10 para 10%).
    :param show: (Opcional) Indica se o retorno deve vir formatado como moeda (True) ou não (False).
    :return: O valor com o aumento aplicado (float ou string formatada).
    """
    valor = n + (n * (aumento / 100))
    if show:
        return moeda(valor)
    else:
        return valor


def diminuir(n, reducao, show=False):
    """
    -> Calcula a redução de um determinado preço, retornando o valor com ou sem formatação.
    :param n: O valor numérico inicial a ser calculado.
    :param reducao: A porcentagem de redução (ex: 15 para 15%).
    :param show: (Opcional) Indica se o retorno deve vir formatado como moeda (True) ou não (False).
    :return: O valor com a redução aplicada (float ou string formatada).
    """
    valor = n - (n * (reducao / 100))
    if show:
        return moeda(valor)
    else:
        return valor


def dobro(n, show=False):
    """
    -> Calcula o dobro de um valor, retornando o resultado com ou sem formatação.
    :param n: O valor numérico a ser duplicado.
    :param show: (Opcional) Indica se o retorno deve vir formatado como moeda (True) ou não (False).
    :return: O dobro do valor (float ou string formatada).
    """
    valor = n * 2
    if show:
        return moeda(valor)
    else:
        return n * 2


def metade(n, show=False):
    """
    -> Calcula a metade de um valor, retornando o resultado com ou sem formatação.
    :param n: O valor numérico a ser dividido.
    :param show: (Opcional) Indica se o retorno deve vir formatado como moeda (True) ou não (False).
    :return: A metade do valor (float ou string formatada).
    """
    valor = n / 2
    if show:
        return moeda(valor)
    else:
        return valor


def moeda(n, moeda="R$"):
    """
    -> Formata um número real para o padrão monetário brasileiro (com vírgula nos centavos).
    :param n: O valor numérico que será formatado.
    :param moeda: O símbolo da moeda que será exibido (padrão é 'R$ ').
    :return: Uma string contendo o valor devidamente formatado (ex: R$ 5,00).
    """
    return f"{moeda}{n:.2f}".replace(".", ",")


def resumo(n, aumento, redução):
    """
    -> Gera e exibe na tela uma tabela com o resumo de todas as operações feitas do módulo.
    :param n: O preço base que será analisado.
    :param aumento: A porcentagem de aumento para exibir na tabela.
    :param redução: A porcentagem de redução para exibir na tabela.
    :return: Não retorna valor (faz apenas a exibição formatada no terminal).
    """
    print(f"""{'-'*36}
{'RESUMO DO VALOR':^36}
{'-'*36}
{'Preço analisdo:':<22}{moeda(n):<13}
{'Dobro do preço:':<22}{dobro(n,True):<13}
{'Metade do preço:':<22}{metade(n,True):<13}
{f'{aumento}% de aumento:':<22}{aumentar(n,aumento,True):<13}
{f'{redução}% de redução:':<22}{diminuir(n,redução,True):<13}
""")

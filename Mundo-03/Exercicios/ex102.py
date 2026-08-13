def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: o valor da fatorial de um número n.
    """
    print("-" * 30)
    lista = []
    resultado = 1
    cont = num

    while cont != 0:

        lista.append(cont)
        resultado *= cont
        cont -= 1

    if show:

        expressão = " x ".join(map(str, lista))
        return f"{expressão} = {resultado}"
    else:

        return resultado


# Program principal
print(fatorial(5, True))

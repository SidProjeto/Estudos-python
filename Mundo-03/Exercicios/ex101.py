def voto(ano_nascimento):
    '''
    -> Calcula a idade de uma pessoa e define sua situação eleitoral.
    :param ano_nascimento: O ano de nascimento da pessoa.
    :return: String com a idade atual e a obrigatoriedade do voto.
    '''
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f"com {idade} anos: NÃO VOTA"
    elif idade < 18 or idade >= 65:
        return f"com {idade} anos: VOTO OPCIONAL"
    else:
        return f"com {idade} anos: VOTO OBRIGATÓRIO"


# programa principal
ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
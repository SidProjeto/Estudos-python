def notas(*notas, sit=False):
    """
    -> função para analisar notas e situação de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não mostrar a situação.
    :return: dicionario com várias informações sobre a situação de turma.
    """
    dados = {}
    maior = menor = media = soma = 0
    print("-" * 30)
    dados["total"] = len(notas)
    for ind, valor in enumerate(notas):
        soma += valor
        if ind == 0:
            maior = valor
            menor = valor
        else:
            if maior < valor:
                maior = valor
            if menor > valor:
                menor = valor
    dados["maior"] = maior
    dados["menor"] = menor
    media = soma / len(notas)
    dados["media"] = media
    if sit:
        if media >= 7:
            dados["situacao"] = "BOA"
        elif media <= 5:
            dados["situacao"] = "RUIM"
        else:
            dados["situacao"] = "RAZOAVEL"
    return dados


# Program Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)

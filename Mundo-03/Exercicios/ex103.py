def ficha(nome="<desconhecido>", gols="0"):
    """
    -> Exibe a ficha de um jogador, mostrando seu nome e o total de gols marcados.
    :param nome: O nome do jogador (opcional, padrão é "<desconhecido>").
    :param gols: A quantidade de gols marcados (opcional, padrão é '0').
    :return: String formatada com a ficha de desempenho do jogador.
    """
    if not nome.isalpha():
        nome = "<desconhecido>"
    if gols == "" or not gols.isdigit():
        gols = "0"
    return f"Jogador {nome} fez {gols} gol(s) no campeonato"


# programa principal
print("-" * 30)
nome = str(input("Nome do Jogador: ")).strip().capitalize()
gols = str(input("Qtd de gols: ")).strip()

print(ficha(nome, gols))

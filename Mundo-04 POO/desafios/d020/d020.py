from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self,nome,nick,):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogo):
        jogoformat = f":video_game: " + jogo.lower()
        if jogoformat in self.jogos_favoritos:
            print(f"[red]O jogo {jogo} ja foi adicionado!")
        else:
            self.jogos_favoritos.append(jogoformat)

    def ficha(self):
        jogos = "\n".join(sorted(self.jogos_favoritos))
        ficha = Panel(
            f"[green]Nome real: [cyan]{self.nome}\n[green]Jogos Favoritos:[cyan]\n{jogos}",title=f"Jogador <{self.nick}>",width=40,)
        print(ficha)


j1 = Gamer("Gustavo", "Cev")
j1.add_favoritos("God of war")
j1.add_favoritos("counter strike 2")
j1.add_favoritos("Fortnite")
j1.add_favoritos("Mario bros")
j1.add_favoritos("sonic")
j1.ficha()

j2 = Gamer("matia", "Rd")
j2.add_favoritos("call of duty")
j2.add_favoritos("Bob esponja")
j2.ficha()

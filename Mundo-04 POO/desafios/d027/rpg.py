from abc import ABC, abstractmethod
from rich import print
from random import randint, choice


class Dado:
    def __init__(self):
        pass

    def rolar(self, lados):
        return {'num':randint(1,lados),'lados':lados}


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.golpes = None

    def atacar(self, alvo, forca):
        if self.vida <= 0:
            print(f"[bold red]{self.nome} está morto[/]!")
            return

        d = Dado().rolar(10)
        dano = int((d["num"] / d["lados"]) * forca)
        print(
            f"[green]{self.nome}[/]({self.vida}) atacou [pink]{alvo.nome}[/]({alvo.vida}) com um [blue]{choice(self.golpes)}[/] de força {forca}"
        )
        print(f"[pink]{alvo.nome}[/] recebeu [red]dano de {dano}[/]!")
        alvo.receber_dano(dano)
        if alvo.vida <= 0:
            print(f"[bold red]{alvo.nome} morreu[/]!")

    def receber_dano(self, dano):
        self.vida -= dano

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de espada", "Ombrada", "Chute"]

    def curar(self):
        if self.vida <= 0:
            print(f"[bold red]{self.nome} está morto[/]")
            return

        if self.vida == self.vida_max:
            print(f"{self.nome} usou uma poção de cura, mas não teve efeito nenhum")

        else:
            d = Dado().rolar(20)
            cura = int((d["num"] / d["lados"]) * self.vida_max)
            if cura + self.vida >= self.vida_max:
                cura = self.vida_max - self.vida
                self.vida = self.vida_max
            else:
                self.vida += cura
            print(f"{self.nome} enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida.")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Míssil Mágico", "Bola de Fogo", "Relâmpago", "Lança de Gelo"]

    def curar(self):
        if self.vida <= 0:
            print(f"[bold red]{self.nome} está morto[/]")
            return

        elif self.vida == self.vida_max:
            print(f"{self.nome} usou magia de cura, mas não teve efeito nenhum")

        else:
            d = Dado().rolar(20)
            cura = int((d["num"] / d["lados"]) * self.vida_max)
            if cura + self.vida > self.vida_max:
                cura = self.vida_max - self.vida
                self.vida = self.vida_max

            else:
                self.vida += cura
            print(f"{self.nome} usou magia de cura e [green]recuperou {cura} pontos[/] de vida.")

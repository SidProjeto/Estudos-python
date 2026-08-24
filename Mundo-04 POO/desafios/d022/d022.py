from rich import print
from rich.panel import Panel
import os


class ControleRemoto:
    def __init__(self):
        self.canal_atual = 1
        self.ligado = False
        self.volume = 0

    def ligar(self):
        if self.ligado:
            self.ligado = False
        else:
            self.ligado = True

    def tv(self):
        if not self.ligado:
            tv = Panel(
                f"[red]\n{'TV Desligada':^19}", title="[ TV ]", width=23, height=5
            )
            return tv
        else:
            tv = Panel(
                f"Canais: {self.canal()}\nVolume: {self.volume_status()}",
                title="[ TV ]",
                width=23,
                height=5,
            )
            return tv

    def canal(self):
        canais = [1, 2, 3, 4, 5]
        canais_formatados = []
        for c in canais:
            if c == self.canal_atual:
                canais_formatados.append(f"[yellow]{c}[/]")
            else:
                canais_formatados.append(str(c))
        resultado = " ".join(canais_formatados)
        return resultado

    def mudar_canal(self, valor):
        if valor < 0:
            valor *= -1
            self.canal_atual -= valor
            if self.canal_atual < 1:
                self.canal_atual = 5
        else:
            self.canal_atual += valor
            if self.canal_atual > 5:
                self.canal_atual = 1

    def volume_status(self):
        volume = [1, 2, 3, 4, 5]
        volume_formatado = []
        bloco = "█"
        for c in volume:
            if c <= self.volume:
                volume_formatado.append(f"[yellow]{bloco}[/]")
            else:
                volume_formatado.append(f"[white]{bloco}[/]")
        resultado = "".join(volume_formatado)
        return resultado

    def mudar_volume(self, valor):
        if valor == "-":
            valor = 1
            self.volume -= valor
            if self.volume <= 0:
                self.volume = 0
        else:
            valor = 1
            self.volume += valor
            if self.volume >= 5:
                self.volume = 5


c = ControleRemoto()
resp = ""
while True:
    os.system("cls")
    if resp == "0":
        break
    print(c.tv())
    resp = str(input(f"< CH{c.canal_atual} > - VOL{c.volume} +  ")).strip()
    if resp == "@":
        c.ligar()
    elif resp == "<" and c.ligado:
        c.mudar_canal(-1)
    elif resp == ">" and c.ligado:
        c.mudar_canal(1)
    elif resp == "+" and c.ligado:
        c.mudar_volume(resp)
    elif resp == "-" and c.ligado:
        c.mudar_volume(resp)

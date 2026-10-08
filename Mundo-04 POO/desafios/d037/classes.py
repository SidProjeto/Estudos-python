from rich import print, box
from rich.panel import Panel

class Mensagem:
    def __init__(self, msg: str = '', tipo: str = '', icone: str = ':speech_balloon:'):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        msg = Panel(f'{self._mensagem}', title=f'{self._icone} AVISO {self._icone}', width=45, border_style='bold white on #000000', style='bold white on #000000', box=box.HEAVY)
        print(msg)



class Erro(Mensagem):
    def __init__(self, msg = '', tipo = '', icone = ':no_entry_sign:'):
        super().__init__(msg, tipo, icone)

    def mostrar(self):
        msg = Panel(f'{self._mensagem}', title=f'{self._icone} ERRO {self._icone}', width=45, border_style='Bold yellow on #FF0000', style='#FFFF00 on #FF0000', box=box.HEAVY)
        print(msg)


class Alerta(Mensagem):
    def __init__(self, msg = '', tipo = '', icone = ':warning:'):
        super().__init__(msg, tipo, icone)

    def mostrar(self):
        msg = Panel(f'{self._mensagem}', title=f'{self._icone} ALERTA {self._icone}', width=45, border_style='#000000 on #FFFF00', style='#000000 on #FFFF00', box=box.HEAVY)
        print(msg)
from rich import box, print
from rich.panel import Panel


class Mensagem:
    def __init__(self, msg:str = '', tipo:str = 'aviso', icone:str = ':speech_balloon:'):
        self._mensagem = msg
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        msg = Panel(f'{self._mensagem}', title=f'{self._icone} {self._tipo.upper()} {self._icone}', width=45, border_style='bold white on #000000', style='bold white on #000000', box=box.HEAVY)
        print(msg)



class Erro(Mensagem):
    def __init__(self, msg:str = ''):
        super().__init__(msg, tipo='erro', icone=':no_entry_sign:')

    def mostrar(self):
        msg = Panel(f'{self._mensagem}', title=f'{self._icone} {self._tipo.upper()} {self._icone}', width=45, border_style='Bold yellow on #FF0000', style='#FFFF00 on #FF0000', box=box.HEAVY)
        print(msg)


class Alerta(Mensagem):
    def __init__(self, msg:str = ''):
        super().__init__(msg, tipo='alerta',icone=':warning:')

    def mostrar(self):
        msg = Panel(f'{self._mensagem}', title=f'{self._icone} {self._tipo.upper()} {self._icone}', width=45, border_style='#000000 on #FFFF00', style='#000000 on #FFFF00', box=box.HEAVY)
        print(msg)
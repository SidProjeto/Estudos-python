from rich import print
from time import sleep


class Livro:
    def __init__(self, titulo, pagina):
        self.titulo = titulo
        self.pagina = pagina
        self.pagina_atual = 1
        print(
            f"[cyan]Você acabou de abrir o livro [green]'{self.titulo}' [cyan]que tem[/] [green]{self.pagina} Paginas[/]\n[cyan]no total. Você agora esta na [green]pagina 1[/]"
        )

    def avancar_paginas(self, avanco=1):
        limite = self.pagina
        cont = 0

        while cont != avanco:

            self.pagina_atual += 1
            if self.pagina_atual > self.pagina:
                self.pagina_atual -= 1
                break

            sleep(0.5)
            print(f"Pág{self.pagina_atual} :arrow_forward: ", end=" ")
            cont += 1

        print(
            f"[cyan]Você avancou {cont} paginas e agora está na [green]pagina {self.pagina_atual}[/]"
        )

        if self.pagina_atual == self.pagina:
            print(
                f":rotating_light:[red] Você chegou ao fim do livro: [green]'{self.titulo}'[/]"
            )

    def __str__(self):
        return f"Nome do livro: {self.titulo} e possui {self.pagina} Paginas"


li = Livro("10 coisas que aprendi", 20)
li.avancar_paginas(5)
li.avancar_paginas(10)
li.avancar_paginas(6)

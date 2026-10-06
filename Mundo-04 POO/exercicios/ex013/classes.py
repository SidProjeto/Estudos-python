class Mae:
    def __init__(self, nome: str = 'mamãe'):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com Leite Condensado e Calda')

    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA Óleo de soja')

class Filha(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com Leite Ninho com Nutella')

class Filho(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA na Air Fryer')
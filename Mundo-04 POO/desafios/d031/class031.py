class Retangulo():
    def __init__(self,base=1,altura=1):
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}'

    @medidas.setter
    def medidas(self,valores):
        self.base = valores[0]
        self.altura = valores[1]
    
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if base < 0:
            raise ValueError('Valor invalido de base!')
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if altura < 0:
            raise ValueError('Valor invalido de altura!')
        else:
            self._altura = altura

    @property
    def area(self):
        return  self._base * self._altura
class Retangulo():
    def __init__(self,base=1,altura=1):
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def medidas(self):
        return f'Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}'

    @medidas.setter
    def medidas(self,valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError('As medidas devem ser informadas dentro de uma tupla')
        
        if len(valores) != 2:
            raise SyntaxError('Informe uma tupla com dois valores numericos')
        
        if isinstance(valores[0], (float, int)):
                self.base = valores[0]
                
        else:
            raise TypeError('A base tem q ser um valor númerico')
        
        if isinstance(valores[1], (float, int)):
                self.altura = valores[1]

        else:
            raise TypeError('A altura tem q ser um valor númerico')
    
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, (float, int)):
            raise ValueError('Valor invalido de base!')
        
        elif base < 0:
            raise ValueError(f'O valor da base não pode ser menor que 0')
        
        else:
            self._base = base
            

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, (float, int)):
            raise ValueError('Valor invalido de altura!')

        elif altura < 0:
            raise ValueError(f'O valor da altura não pode ser menor que 0')
        
        else:
            self._altura = altura
            

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self, valor):
        raise PermissionError('A area não pode ser alterada')
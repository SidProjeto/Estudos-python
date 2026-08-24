# Declaração de Class
class Gafanhoto:
    """
    Essa Classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

    para criar uma nova pessoa, use
    variavel = gafanhoto(nome,idade)
    """

    def __init__(self, nome="vazio", idade=0):  # Método construtor
        # Atributo de Instância
        self.nome = nome
        self.idade = idade

    # métodos de instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self):  # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()

print(g1.__doc__)  # Dunder Attribute
print(g1)
print(g1.__dict__)  #Atributo
print(g1.__getstate__())    #metodo
print(g1.__class__) 
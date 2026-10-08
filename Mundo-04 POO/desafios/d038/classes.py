from locale import setlocale, LC_ALL, currency

setlocale(LC_ALL, 'pt_BR.UTF-8')

class Carrinho:
    def __init__(self):
       self.produtos = []

    @property
    def total(self):
        total = 0
        for produto in self.produtos:
            total += produto['preco']

        return currency(total, grouping=True)

    def dict_produto(self, produto):
        if isinstance(produto, Produto):
            produto_dict = {
            'nome': produto.nome,
            'preco': produto.preco
            }
            self.produtos.append(produto_dict)
        
    def __add__(self, produto):
        if isinstance(produto, Carrinho):
            self.produtos.extend(produto.produtos)
        else:
            self.dict_produto(produto)
            
        return self
    
    def __iadd__(self, produto):
        if isinstance(produto, Carrinho):
            self.produtos.extend(produto.produtos)
        else:
            self.dict_produto(produto)

        return self

    def __str__(self):
        msg = f'{30*'-'}\n'
        for produto in self.produtos:
            msg += f"{produto['nome'].title()} ({currency(produto['preco'], grouping=True)})\n"
        msg += f'{30*'-'}\n'
        msg += f'Total: {self.total}\n'
        return msg


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} ({currency(self.preco, grouping=True)})'
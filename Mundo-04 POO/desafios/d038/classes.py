from locale import setlocale, LC_ALL, currency

setlocale(LC_ALL, "pt_BR.UTF-8")


class Carrinho:
    def __init__(self):
        self.produtos = []

    @property
    def total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco

        return currency(total, grouping=True)


    def __add__(self, produto):
        novo_carrinho = Carrinho()
        novo_carrinho.produtos.extend(self.produtos)

        if isinstance(produto, Carrinho):
            novo_carrinho.produtos.extend(produto.produtos)

        elif isinstance(produto, Produto):
            novo_carrinho.produtos.append(produto)

        else:
            raise TypeError(f'Não é possivel somar ao carrinho o {type(produto).__name__}')
        
        return novo_carrinho

    def __iadd__(self, produto):
        if isinstance(produto, Carrinho):
            self.produtos.extend(produto.produtos)

        elif isinstance(produto, Produto):
            self.produtos.append(produto)

        else:
            raise TypeError(f'Não é possivel somar ao carrinho o {type(produto).__name__}')
        
        return self

    def __str__(self):
        msg = f"{30*'-'}\n"

        for produto in self.produtos:
            msg += f"{produto}\n"

        msg += f"{30*'-'}\n"
        msg += f"Total: {self.total}\n"

        return msg


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome

        if isinstance(preco, bool):
            raise ValueError(f'Valor invalido!')
        
        try:
            self.preco = float(preco)

        except (ValueError, TypeError):
            raise ValueError(f'Valor invalido!')


    def __str__(self):
        return f"{self.nome} ({currency(self.preco, grouping=True)})"

    def __repr__(self):
        return self.__str__()

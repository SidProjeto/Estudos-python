'''def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input("digite um número: "))
if par(num):
    print("par")
else:
    print("impar")'''


"""def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input("Digite um número: "))
print(f"O fatorial de {n} é {fatorial(n)}")"""


"""def teste(b):
    global a # muda o A global
    a = 8
    b += 4
    c = 2
    print(f"A dento vale {a}")  # escopo global / sem 'global a' é escopo local
    print(f"B dento vale {b}")  # escopo local
    print(f"C dento vale {c}")  # escopo local


# Program Principal
a = 5  # a escopo global
teste(a)
print(f"A Fora vale {a}")  # global"""


"""def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(8, 4)
r3 = somar(4)
print(f'Os resultados foram {r1}, {r2}, {r3}')"""


"""'def contador(i,f,p):
    
    # -> faz uma contagem na tela-
    # :PARA I: inicio da contagem
    # :PARA F: fim da contagem
    # :para p: passo da contagem
    # :return: sem retorno

    
    c = i
    while c <= f:
        print(f'{c}',end=' ')
        c += p
contador(1,10,2)
help(contador)"""

from time import sleep


def contador(inicio, fim, passo):
    passo_exib = passo
    fim_range = fim

    if inicio > fim:
        fim_range -= 1
        if passo > 0:
            passo *= -1
    else:
        fim_range += 1
        if passo < 0:
            passo *= -1
            passo_exib *= -1
    print("-=" * 20)
    print(f"Contagem de {inicio} até {fim} de {passo_exib} em {passo_exib}: ")
    for valor in range(inicio, fim_range, passo):
        print(valor, end=" ", flush=True)
        sleep(0.5)
    print("FIM!")
    print("-=" * 20)


contador(1, 10, 1)
contador(10, 0, 2)

print("-=" * 20)
print("Agora é sua vez de personalizar!")
num1 = int(input("Valor do inicio: "))
num2 = int(input("Valor do final: "))
num3 = int(input("Valor do passo: "))
if num3 == 0:
        print("Erro! passo não pode ser 0")
        while num3 == 0:
            num3 = int(input("Passo: "))
contador(num1, num2, num3)

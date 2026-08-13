def escreva(text):
    tam = len(text) + 4
    print("~" * tam)
    print(f"{text:^{tam}}")
    print("~" * tam)


for i in range(3):
    texto = str(input(f"Texto{i + 1}: "))
    escreva(texto)
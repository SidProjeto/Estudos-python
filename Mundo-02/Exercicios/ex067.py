from time import sleep
while True:
    tabuada = int(input('Qual tabuada você quer ver? '))
    if tabuada < 0:
        break
    print (f'=== Tabuada do {tabuada} ===')
    for c in range(1,11):
        print(f'{tabuada} x {c:2} = {tabuada * c}')
        sleep(0.5)
    print('=' * 19)
print('Programa encerrado')
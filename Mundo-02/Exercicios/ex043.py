from time import sleep
print('\033[1;33mCalculador de IMC\033[0m')
peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso/altura**2
print('\033[1;36mCalculando IMC...\033[0m')
sleep(3)
print(f'seu IMC é de {imc:.1f}')
if imc < 18.5:
    print('Você está \033[1;33m Baixo do Peso\033[0m')
elif imc >= 18.5 and imc < 25:
    print('Você está no \033[1;33m Peso Ideal\033[0m')
elif imc >= 25 and imc < 30:
    print('Você está com \033[1;33mSobrepeso\033[0m')
elif imc >= 30 and imc < 40:
    print('Você está com \033[1;33mObesidade\033[0m')
elif imc >= 40:
    print('Você está com \033[1;33mObesidade Mórbida\033[0m')
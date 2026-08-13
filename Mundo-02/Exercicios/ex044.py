print('\033[1;33mCalculador de valor a ser pago\033[0m')
preco = float(input('Digite o preço do produto: R$'))
pagamento = int(input('Digite sua forma de pagamento:\n1 para à vista Dinheiro/Cheque\n2 para à vista com cartão\n3 Cartão parcelado\nSua opção:   '))
if pagamento == 3:
    parcelado = int(input('Ira parcelar em quantas vezes? '))
    if parcelado == 2:
        valor = preco / parcelado
        print(f'Você ira pagar parcelas de R${valor:.2f}')
    else:
        valor = preco / parcelado
        print(f'Você ira pagar parcelas de R${valor+(valor *20/100):.2f}')
elif pagamento == 2:
    print(f'Você vai pagar R${preco-(preco*5/100):.2f}')
elif pagamento == 1:
    print(f'Você vai pagar R${preco-(preco*10/100):.2f}')  
else:
    print('\033[1;31mOpção invalida de pagamento, tente novamente!\033[0m')
print('\033[1:33m''Conversor de R$ para US$,Eur€,JPY¥ ,ARS$')
m = float(input('Quanto você possui? R$'))
d = m / 3.27
e = m / 6.01
i = m /0.033
p = m / 0.0038
print(f'{'\033[1:36m'}Você pode comprar \nUS${d:.2f}\nEUR€{e:.2f}\nJPY¥{i:.2f}\nARS${p:.2f}')

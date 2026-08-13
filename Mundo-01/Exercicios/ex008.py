print('\033[1:33m''Conversor de Metros para centímetros e milímetros')
m = float(input('Distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'Você tem {m} metros, convertendo você tem:\n{km}quilômetros\n{hm}Hectômetro')
print(f'{dam:.0f}Decâmetro\n{dm:.0f}Decímetro\n{cm:.0f} centímetros\n{mm:.0f} milímetros')

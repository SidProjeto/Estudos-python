print('soma de ímpares multiplos de 3(1-500)')
s = 0
t = 0
for c in range(1,501, 2):
    if c % 3 == 0:
       s += c 
       t += 1  
print(f'Soma de {t} dos valores é {s}')
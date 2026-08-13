print('Tabuada')
num = int(input('Digite número: '))
print('\033[1;33m='*5,'TABUADA','='*5)
for t in range(1,11):
    print(f'{num} x {t:2} == {num*t}')
print('='*19,'\033[0m')
from datetime import date
print('\033[1;33m''Categoria do atleta de natação''\033[0m')
ano = int(input('Ano de nascimento: '))
data = date.today().year
if data - ano <= 9:
    print('Categoria \033[1;36mMIRIM\033[0m')
elif data - ano >=10 and data - ano <= 14:
    print('Categoria \033[1;36mINFANTIL\033[0m')
elif data - ano >= 15 and data - ano <= 19:
    print('Categoria \033[1;33mJUNIOR\033[0m')
elif data - ano >= 20 and data - ano <= 25:
    print('Categoria \033[1;36mSÊNIOR\033[0m')
elif data - ano >=26:
    print('Categoria \033[1;36mMASTER\033[0m')
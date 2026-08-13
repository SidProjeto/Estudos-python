city = str(input('nome da cidade: ')).strip()
print(f'possui santo: {city.capitalize().split()[0] == 'Santo'}')
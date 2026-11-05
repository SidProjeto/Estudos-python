import sqlite3
from datetime import date

busca = input("Quem você está procurando? ").strip()
hoje = date.today()

try:
    with sqlite3.connect("meubanco.db") as banco:
        banco.row_factory = sqlite3.Row
        cur = banco.cursor()

        cur.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))


        total = 0
        for total, amigo in enumerate(cur, start=1):
            idade = 0
            nasc = str(amigo["nascimento"]).strip()

            if nasc == "" or date == None:
                info_nasc = "Sem data de nascimento"

            else:
                try:
                    data = date.fromisoformat(nasc)
                    
                    japassou = (hoje.month, hoje.day) >= (data.month, data.day)
                    idade = hoje.year - data.year - ( 0 if japassou else 1)

                    info_nasc = f'nasceu em {data:%d/%m/%Y} e tem {idade} anos'

                except ValueError:
                    info_nasc = "data inválida"

            print(f"{amigo['nome']} {info_nasc}")
        print('-' * 50)
        if total >= 1:
            if total == 1:
                print(f"Encontrei apenas {total} amigo com '{busca}'")

            else:
               print(f"Ao todo encontrei {total} amigos com '{busca}'")

        else:
            print(f"Não encontrei ninguém com '{busca}' no nome!")

except sqlite3.Error as e:
    print(f"Falha no banco: {e}")

except Exception as e:
    print(f"Algo deu errado: {e}")

from time import sleep


def maior(*num):
    print("-=" * 20)
    if len(num) == 0:
        print("Não foi infomado nenhum valor")
    else:
        pos = m = 0
        print("Analisando valores passados...")
        while pos < len(num):

            print(num[pos], end=" ", flush=True)
            sleep(0.5)
            if pos == 0:
                m = num[pos]
            else:
                if m < num[pos]:
                    m = num[pos]
            pos += 1
        print(f"foram imformados {len(num)} valores ao todo.")
        print(f"O maior valor informado é {m}")


maior(2, 9,4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

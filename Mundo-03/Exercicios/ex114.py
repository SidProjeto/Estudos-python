def testar_url(url):
    import requests
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            print(f"\033[1;32mConsegui acessar o site: \'{resp.url}\' com sucesso!\033[m")
        else:
            print(f"Não consegui acessar o site \'{resp.url}\'")
            
    except requests.exceptions.ConnectionError:
        print('\033[1;31mERRO: Conecte-se com a internet:\033[m')
        
    except (ValueError, TypeError,requests.exceptions.RequestException):
        print("\033[1;31mERRO: Você colocou o valor errado ou esqueceu do \'https://\'!\033[m")
   
    

try:
    site = str(input('Qual site deseja verificar? ')).strip()
    testar_url(site)

except KeyboardInterrupt:
    print('\n\033[1;33mO usuario encerrou sem informar o dado\033[m')

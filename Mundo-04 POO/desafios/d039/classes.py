from abc import ABC, abstractmethod


class Validador(ABC):

    @abstractmethod
    def validar(self, valor):
        pass


class Usuario(Validador):

    def validar(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O nome de Usuário deve ser uma string")

        if not (5 <= len(valor) <= 20):
            raise ValueError("O nome de Usuário deve conter entre 5 a 20 caracteres")

        if any(letra.isupper() for letra in valor):
            raise ValueError("O nome de usuário so suporta letras minúsculas")

        if not valor.replace("_", "").isalnum():
            raise ValueError("O nome de usuário permite apenas o sublinhado (_) como caractere especial")

        return True


class Email(Validador):
    especias = ['@','.','+','-','_']

    def validar(self, valor):
        if not isinstance(valor, str):
            raise TypeError("O email deve ser uma string")

        if valor.count('@') != 1:
            raise ValueError("O email deve conter uma única @")
        
        for letra in valor:
            if not letra.isalnum() and  letra not in Email.especias:
                raise ValueError("O e-mail contém caracteres especiais inválidos!")
            
        local, dominio = valor.split('@')
        if len(local.strip()) == 0:
            raise ValueError("O e-mail deve conter caracteres antes do @")
        
        if  '.' not in dominio:
            raise ValueError("O e-mail deve conter uma extensão de domínio válida (ex: .com)")
        
        if len(dominio.split('.')[0].strip()) == 0:
            raise ValueError("O e-mail deve conter o nome do provedor após o @")
        
        tld = dominio.split('.')[-1]
        if not len(tld.strip()) >= 2:
            raise ValueError("A extensão final do e-mail é inválida")

        return True

class Senha(Validador):

    def validar(self, valor):
        if not isinstance(valor, str):
            raise TypeError("A senha deve ser uma string")

        if not (len(valor) >= 8):
            raise ValueError('A senha deve conter no mínimo 8 caracteres')

        if not any(letra.isupper() for letra in valor):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")

        if not any(letra.islower() for letra in valor):
            raise ValueError("A senha deve conter pelo menos uma letra minúscula.")

        if not any(letra.isdigit() for letra in valor):
            raise ValueError('A senha deve conter pelo menos um número.')

        if not any(not letra.isalnum() for letra in valor):
            raise ValueError("A senha deve conter pelo menos um caractere especial (símbolo).")

        return True

def validar_dado(validador, valor):
    vali = None
    motivo = None
    try:
        validador.validar(valor)
        vali = 'SIM'

    except Exception as e:
        vali = 'NÂO'
        motivo = e

    print(f'Valor: {valor} é valido: {vali}')
    if motivo:
        print(f'Motivo: {motivo}')



    

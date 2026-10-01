from abc import ABC
from datetime import date

class Pessoa(ABC):
    ano_limite = date.today().year - 130
    def __init__(self,nome: str, ano: int):
        self._nome = nome

        if Pessoa.ano_limite <= ano <= date.today().year:
            self._nascimento = ano

        else:
            raise ValueError(f'Ano {ano} é invalido')

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano: int):
        ano = abs(ano)
        if Pessoa.ano_limite <= ano <= date.today().year:
            self._nascimento = ano

        else:
            raise ValueError(f'Ano {ano} é invalido')

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor: int):
        raise PermissionError('Idade não pode ser alterada')


class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
    def __init__(self, nome, ano, curso):
        super().__init__(nome, ano)
        curso = curso.upper()
        if curso in Aluno.cursos_oficiais:
            self._curso = curso

        else:
            raise ValueError(f"O curso '{curso}' não está na lista de cursos oficiais")

    def adicionar_curso(self, nome_curso: str):
        if 3 <= len(nome_curso) <= 5:
            nome_curso = nome_curso.upper()
            if nome_curso in Aluno.cursos_oficiais:
                raise ValueError('Esse curso ja está na lista')
            else:
                Aluno.cursos_oficiais.append(nome_curso)
        else:
            raise ValueError('encurte nome do curso!')

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso: str):
        curso = curso.upper()
        if curso in Aluno.cursos_oficiais:
            self._curso = curso

        else:
            raise ValueError(f"O curso '{curso}' não está na lista de cursos oficiais")
    
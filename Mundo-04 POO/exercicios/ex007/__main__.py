from rich import print, inspect
from classes import Aluno, Professor, Funcionario,Pessoa

def main():
    a1 = Aluno("José", 17, "Informatica", "T01")
    a1.fazer_anivesario()
    a1.fazer_matricula()

    p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
    p1.fazer_anivesario()
    p1.dar_aula()

    f1 = Funcionario("Claudia", 27, 'secretária', 'secretaria')
    f1.fazer_anivesario()
    f1.bater_ponto()

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == "__main__":
    main()
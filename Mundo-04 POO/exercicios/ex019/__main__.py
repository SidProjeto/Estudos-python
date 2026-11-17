from crud import *
from rich import print
from sistema import *


def main():

    # cadastro_em_massa() #[IMPORTANTE] Execute apenas uma vez

    if not criar_banco():
        print("[red]Algum problema aconteceu ao criar banco[/]")
        raise SystemExit

    while True:
        resp = menu()

        match resp:
            case "1":  # Cadastrar pessoa
                if not cadastrar_pessoa():
                    print("[red][ERRO] Não foi possível cadastrar a pessoa[/]")

            case "2":  # Listar pessoas
                if not listar_pessoa():
                    print("[red][ERRO] Não foi possível mostrar a listagem[/]")

            case "3":  # Atualizar pessoa
                if not atualizar_pessoa():
                    print("[red][ERRO] Não foi possível atualizar o cadastro[/]")

            case "4":  # Excluir pessoa
                if not excluir_pessoa():
                    print("[red][ERRO] Não foi possível excluir a pessoa[/]")

            case "5":  # Busca por nome
                if not buscar_pessoa_por_nome():
                    print("[red][ERRO] Não foi possível buscar os dados[/]")

            case "0":  # Sair
                print("\n[orange_red1]Encerrando o sistema...[/]")
                break

            case _:
                print("\n[red][ERRO] Opção inválida! Escolha um valor entre 0 e 5![/]")

        input(f"\n{color['orange']}Pressione ENTER para continuar...{color['limpo']}")


if __name__ == "__main__":
    main()

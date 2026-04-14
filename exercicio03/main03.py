from .encapsulamento.aluno_info03 import aluno
alu = aluno()
def menu():
    print("1 - cadastrar aluno")
    print("2 - aualizar senha: ")
    print("3 -  mostrar senha")
    print("4 - mostrar matricula")

def main03():
    while True:
        menu()
        opcao = input("opcao: ")
        match opcao:
            case "1":
                alu.nome = input("nome: ")
                alu.senha = int(input("senha: "))
                if len(alu.senha) < 6:
                    raise ValueError("Erro: tamanho de senha inválida (minimo 6 digitos)")
                else:
                 alu.matricula = int(input("matricula: "))
            case "2":
                if not alu.senha:
                    raise ValueError("Erro: senha não existe. Cadastre uma antes, para que possa modifica-la")
                alu.set_senha()

            case "3":
                if not alu.senha:
                    raise ValueError("Erro: senha não existente")
                alu.mostrar_senha()
            case "4":
                alu.mostrar_matricula()

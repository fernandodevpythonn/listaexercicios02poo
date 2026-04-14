from .encapsulamento.aluno_info import aluno
alu = aluno()
def menu():
    print("1 - cadastrar aluno")
    print("2 -  mostrar senha")
    print("3 - mostrar matricula")

def main01():
    while True:
        menu()
        opcao = input("opcao: ")
        match opcao:
            case "1":
                alu.nome = input("nome: ")
                alu.senha = int(input("senha: "))
                alu.matricula = int(input("matricula: "))
            case "2":
                alu.mostrar_senha()
            case "3":
                alu.mostrar_matricula()

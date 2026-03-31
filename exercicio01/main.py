from encapsulamento.aluno import aluno
alu = aluno()
def menu():
    print("1 - adicionar matricula")
    print("2 - mostrar matricula")
    print("3 - mostrar senha")

def main():
    while True:
        menu()
        opcao = input("opcao: ")
        match opcao:
            case "1":
                alu.matricula = int(input("matricula: "))
            case "2":
                alu.mostrar_matricula()
            case "3":
                alu.mostrar_senha()
main()
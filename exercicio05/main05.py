from .funcionario.funcionario_info import Funcionario
fun = Funcionario()
def menu():
    print("1 - adicionar dados")
    print("2 - mostrar dados")
    print("3 - mostrar salário")

def main05():
    while True:
        menu()
        opcao = input("Digite uma opção: ")
        match opcao:
            case "1":
             fun.adicionar_dados()
            case "2":
              fun.mostrar_detalhes()
            case "3":
              fun.mostrar_salario()
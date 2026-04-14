from modulos import *

def menu():
    print("1 - Exercício 01")
    print("2 - Exercício 02")
    print("3 - Exercício 03")
    print("4 - Exercício 04")
    print("5 - Exercício 05")
    print("6 - Exercício 06")
def main():
    while True:
        menu()
        opcao = input("Escolha um exercício: ")
        match opcao:
            case "1":
                main01()
            case "2":
                main02()
            case "3":
                main03()
            case "4":
                main04()
            case "5":
                main05()
            case "6":
                main06()
if __name__ == "__main__":
    main()
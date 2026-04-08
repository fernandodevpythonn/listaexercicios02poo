from banco_info.banco import ContaBancaria
conta = ContaBancaria()
def menu():
    print("1 - mostrar senha")
    print("2 - atualizar senha")
def main():
    while True:
        menu()
        opcao = input("escolha uma opção: ")
        match opcao:
            case "1":
                conta.get_senha()
            case "2":
                conta.set_senha()


if __name__ == "__main__":
    main()
from .cofre.cofre_info import cofre
cof = cofre()
def menu():
    print("====== Segredo ======")
    print("1 - Atualizar segredo")
    print("2 - Mostrar histórico")
    print("3 - mostrar segredo")
def main06():
    while True:
        menu()
        opcao = input("escolha uma opção: ")
        match opcao:
            case "1":
                cof.alterar_segredo()
            case "2":
                cof.mostrar_historico()
            case "3":
                cof.mostrar_segredo()
                
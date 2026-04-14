class cofre:
    def __init__(self):
        self.__segredo = "fernando123"
        self.__historico = []
    
    @property
    def segredo(self):
        return self.__segredo
    @segredo.setter
    def segredo(self,valor):
        segredo_padrao = valor
        self.__segredo = segredo_padrao

    @property
    def historico(self):
        return self.__historico
    @historico.setter
    def historico(self,valor):
        historico_padrao = valor
        self.__historico = historico_padrao

    def mostrar_segredo(self):
        """mostra o segredo"""
        print(self.segredo)

    def alterar_segredo(self):
        """altera o segredo"""
        novo_segredo = input("Digite um novo segredo")
        if novo_segredo != self.segredo:
         self.historico.append(self.segredo)
         self.segredo = novo_segredo
         print(f"Novo segredo: {novo_segredo}")
        else:
            raise ValueError("Erro: digite um segredo diferente do antigo")

    def mostrar_historico(self):
        """mostra o histórico de segredos"""
        for segredo in self.historico:
            print(segredo)
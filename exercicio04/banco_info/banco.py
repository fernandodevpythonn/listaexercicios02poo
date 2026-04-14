class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,valor):
        saldo_cli = valor
        self.__saldo = saldo_cli

    def get_senha(self):
        """mostra a senha"""
        print(self.saldo)
    def set_senha(self):
        """altera a senha"""
        self.senha = input("Atualizar senha(minimo 6 caracteres): ")
        if len(self.senha) < 6:
            raise ValueError("Erro: Digite uma senha com mais de 6 caracteres")
        elif self.senha.isalpha():
            raise ValueError("Erro: Digite uma senha do tipo inteiro")
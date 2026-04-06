class aluno:
    def __init__(self,nome = "sem nome"):
        self.nome = nome
        self.__matricula = ""
        self.__senha = ""
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,valor):
        matricula_alu = valor
        self.__matricula = matricula_alu

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self,valor):
        senha_alu = valor
        self.__senha = senha_alu

    def mostrar_senha(self):
        print(f"Senha: {self.senha}")
    def mostrar_matricula(self):
        print(f"Matricula: {self.matricula}")

class aluno:
    def __init__(self, nome = "sem nome"):
        self.__matricula
        self.nome = nome
        self.__senha
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,valor):
        matricula_in = valor
        self.__matricula = matricula_in

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self,valor):
        valor = 181818
        senha_aluno = valor
        self.senha = senha_aluno

    def mostrar_senha(self):
        print(f"Senha: {self.matricula}")
    def mostrar_matricula(self):
        print(f"Matricula: {self.matricula}")
    
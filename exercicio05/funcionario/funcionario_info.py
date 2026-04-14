class Funcionario:
    def __init__(self, nome = "sem nome"):
        self.nome = nome
        self.__cargo = ""
        self.__salario = 0
    @property
    def cargo(self):
        return self.__cargo
    @cargo.setter
    def cargo(self,valor):
        cargo_atual = valor
        self.__cargo = cargo_atual
    
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self,valor):
        salario_atual = valor
        self.__salario = salario_atual
    
    def adicionar_dados(self):
        """adiciona os dados do funcionário"""
        self.nome = input("Nome:")
        if self.nome.isalpha():
            print(f"Nome {self.nome} adicionado")
        else:
            raise ValueError("Erro: nome inválido")
        try:
         self.cargo = input("Cargo: ")
         if not self.cargo.isdigit():
          print(f"Cargo {self.cargo} adicionado")
        except ValueError:
            print("Erro: valor inválido")
        try:
          self.salario = float(input("Salário: "))
          if self.salario > 0:
              print(f"Salário {self.salario} adicionado")
        except ValueError:
            print("erro: valor inválido")

    def mostrar_detalhes(self):
        """mostra os detalhes do funcionário"""
        print(self.nome)
        print(self.cargo)
        print(self.salario)
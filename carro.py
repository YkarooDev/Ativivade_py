class Carro:
    def mostrar_marca(self):
        print(f"A marca do carro e: {self.marca}")

    def mostrar_modelo(self):
        print(f"O modelo e: {self.modelo}")

    def mostrar_ano(self):
        print(f"Ano do veiculo: {self.ano}")

    def mostrar_potencia(self):
        print(f"A potencia do seu carro e: {self.potencia}")
        if (self.potencia == 1.0):
            print(f"O seu carro nao anda nada vei!!! ")

    def mostrar_caracteristicas(self):
        self.mostrar_marca()
        self.mostrar_modelo()
        self.mostrar_ano()
        self.mostrar_potencia()

class Propietario:
    def mostrar_nome(self):
        print(f"O propietario do veiculo e: {self.nome}")

    def mostrar_idade(self):
        print(f"Idade: {self.idade}")

    def mostrar_endereco(self):
        print(f"Endereco: {self.endereco}")

    def mostrar_dados(self):
        self.mostrar_nome()
        self.mostrar_idade()
        self.mostrar_endereco()
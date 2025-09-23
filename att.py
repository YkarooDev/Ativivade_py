class Carro:
    def mostrar_marca(self):
        print(f"A marca do seu carro e: {self.marca}")

    def mostrar_modelo(self):
        print(f"E o modelo do seu carro e: {self.modelo}")

    def mostrar_ano(self):
        print(f"O ano do seu veiculo e: {self.ano}")

    def mostrar_potencia(self):
        print(f"A potencia do seu carro e: {self.potencia}")
        if (self.potencia == 1.0):
            print(f"O seu carro nao anda nada vei!!! ")

    def mostrar_tudo(self):
        self.mostrar_marca()
        self.mostrar_modelo()
        self.mostrar_ano()
        self.mostrar_potencia()


meu_carro = Carro()

meu_carro.marca = "Wolksvagen"
meu_carro.modelo = "Gol quadrado"
meu_carro.ano = 1992
meu_carro.potencia = 1.8

meu_carro.mostrar_tudo()

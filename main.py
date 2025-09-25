from carro import Carro, Propietario

meu_carro = Carro()
meu_carro.marca = "Wolksvagen"
meu_carro.modelo = "Gol quadrado"
meu_carro.ano = 1992
meu_carro.potencia = 1.8

dono = Propietario()
dono.nome = "Paulo"
dono.idade = 23
dono.endereco = "Rua dos bobos."

dono.mostrar_dados()
meu_carro.mostrar_caracteristicas()
## PetShop.py


class Cliente:
  def __init__(self, nome, raca, peso, idade):
    self.nome = nome
    self.raca = raca
    self.peso = peso
    self.idade = idade

  def __str__(self):
    return f'Nome: {self.nome}, raça: {self.raca}, peso: {self.peso}, idade: {self.idade}'

class Servico:
  def __init__(self, tosa, banho):
    self.tosa = tosa
    self.banho = banho

  def __str__(self):
    return f'Tosa: {self.tosa}, banho: {self.banho}'

class Produtos:
  class alimento:
    def __init__(self, comida, bebida):
      self.comida = comida
      self.bebida = bebida
    def __str__(self):
      return f'Comida: {self.comida}, bebida: {self.bebida}'

  class medicamento:
    def __init__(self, medicamento):
      self.medicamento = medicamento

    def __str__(self):
      return f'Medicamento: {self.medicamento}'

  class brinquedos:
    def __init__(self, brinquedos):
      self.brinquedos = brinquedos

    def __str__(self):
      return f'Brinquedos: {self.brinquedos}'


nome_pet = input("Informe o nome do pet: ")
raca_pet = input("Informe a raça do pet: ")
peso_pet = input("Informe o peso do pet: ")
idade_pet = int(input("Informe a idade do pet: "))

cliente1 = Cliente(nome_pet, raca_pet, peso_pet, idade_pet)


print(cliente1)
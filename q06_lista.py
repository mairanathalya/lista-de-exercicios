# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

Idade = []
Altura = []

for i in range(0,5):
  Idade = int (input('Qual a sua idade? '))
  Altura = float (input('Qual a sua altura? '))
  Idade.append(Idade)
  Altura.append(Altura)

 #fazendo a ordem inversa  
print("Ordem inversa")
print("Altura")
print(Altura[::-1])

print("Idade")
print(Idade[::-1])

#fazendo a ordem lida

print("Ordem lida")
print("Altura: ")

print("Ordem lida")
print("Idade: ")
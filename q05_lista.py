# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.


numero = int (input("Escolha um número: "))
lista =[]

for i in range(1 + numero):
  if (i % 2 == 1) and (i != 2):
    lista.append(i)
print(f"números {lista}")
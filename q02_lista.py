#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

from random import randint


nota = float (input("Digite uma nota:  "))

while (nota < 0 or nota > 10):
  print("Valor inválido, tente novamente")
  nota = float (input("Digite uma nota:  "))

else:
  print("Valor válido!!!")
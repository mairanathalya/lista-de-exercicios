# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int (input("Digite um ano: "))
bissexto = ''

if (ano % 4)== 0 and (ano % 100)==0 and (ano % 400)==0:
  print("Este ano é bissexto!!!")
  bissexto = True
elif (ano % 4) != 0:
  print("Este ano não é bissexto")
  bissexto = False
elif (ano % 4)== 0 and (ano % 100) != 0:
  print("Este ano é bissexto!!!")
  bissexto = True
elif (ano % 4)== 0 and (ano % 100)==0 and (ano % 400)!=0:
  print("Este ano não é bissexto")
  bissexto = False
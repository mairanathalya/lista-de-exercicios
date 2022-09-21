# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.

def reverso(numero):
  return  str (numero[::-1])
numero = str (input("Digite um número: "))
  
print(f"O reverso do número é : {reverso(numero)}")
#Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# c) A mensagem "Aprovado com Distinção", se a média for igual a 10


n1 = float (input("Digite a primeira nota: "))
n2 = float (input("Digite a segunda nota: "))
n3 = float (input("Digite a terceira nota: "))
media = float (n1 + n2 + n3)/ 2

if (media >= 7):
    print(f"Você foi Aprovado com média " , {media})
elif (media < 7):
    print(f"Você foi Reprovado com média " , {media})
elif(media == 10):
    print(f"Você foi Aprovado com distinção!" , {media})
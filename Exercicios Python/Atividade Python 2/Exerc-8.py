nome = str(input('Digite o seu nome: '))
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

media = (n1 + n2 + n3) / 3

if media >= 8:
    print("Parabéns ", nome,"! Voce foi aprovado")

elif media >= 5:
    print ("Voce ficou com média de ", media, " e esta de recuperação")

else:
    print (nome,", voce esta reprovado")
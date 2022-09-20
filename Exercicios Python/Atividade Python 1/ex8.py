media = int(input('Digite a média: '))
freq = int(input('Digite a frequência: '))

if freq < 75:
    print('Você foi reprovado!')
if freq > 75 and media < 7:
    print('Você está de recuperação!')
if freq > 75 and media >= 7:
    print ('Você foi aprovado!')










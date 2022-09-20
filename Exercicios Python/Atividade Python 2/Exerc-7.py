from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0
for pessoa in range(1, 11):

    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc

    if idade >= 18:
        tmaior += 1
    else:
        tmenor += 1

print(f'Ao todo tivemos {tmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {tmenor} pessoas menores de idade')
print('Programa Encerrado')
sal = float(input('Digite o valor do sálario: '))

if sal <= 1903.98:
    print ('Isento')

if sal >= 1903.99 and sal <= 2826.65:
    print ('7,5% - R$142,80')

if sal >= 2826.66 and sal <= 3751.05:
    print ('15% - R$354,80')

if sal >= 3751.06 and sal <= 4664.68:
    print ('22,5% - R$636,13')

if sal > 4664.68:
    print ('27,5% - R$869,36')












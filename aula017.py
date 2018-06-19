sal = float(input(' qual é o seu salario: '))
if sal > 1250.00:
    newsal = (sal + (sal * 10) / 100)
    print ('Seu salario de: ', sal,'R$, com o almento de 10% , passara a ser de:', newsal,'R$')
if sal <= 1250.00:
    newsal = (sal + (sal * 15) / 100)
    print ('Su salario de {:.2f}R$, com o almento de 15%, passara a ser de {:.2f}R$'.format(sal, newsal))


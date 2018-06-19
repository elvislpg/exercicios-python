r1 = int(input('digite um valor '))
r2 = int(input('outro '))
r3 = int(input('mais um '))
if  r1 < r2 + r3  and r2 < r1 + r3 and r3 < r2 + r1 :
    print(' faz um triangulo')
else:
    print ('não pode formar um triangulo')
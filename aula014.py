distancia = float(input(' qual a distancia em KM: '))
if distancia <= 200:
    print('o preco da passagem é ', distancia * 0.50)
else:
    print ('o valor da passagem é: ', distancia * 0.45)
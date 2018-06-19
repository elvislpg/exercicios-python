velocidade = int(input('qual foi sua velocidade '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(' vc foi multado ')
    print(' vc deve pagar uma multa de {} '.format(multa))

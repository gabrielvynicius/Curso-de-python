km = int(input('Quantos Km você passou no radar? '))
if km > 80:
    print(f'Você utrapassou o limite da via e infelizmente vai precisar pagar uma multa no valor de R$ {7*(km -80)}')
else:
    print('Show voce não utrapasso o limite de velocidade.')
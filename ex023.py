num = int(input('Digite Um valor de 0 a 9999: '))
print('''Sobre o numero digitado...
Sua parte de Unidade: {}
Sua parte de Dezena : {}
Sua parte de Centena: {}
Sua parte de Milhar : {}'''.format(num // 1 % 10, num // 10 % 10, num // 100 % 10, num // 1000 % 10))

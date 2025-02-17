#from math import sqrt, pow
#n1 = float(input('Comprimento do cateto oposto: '))
#n2 = float(input('Comprimento do cateto adjacente: '))
#print('A hipotenusa vai medir {:.2f}'.format(sqrt((n1**2) + (n2**2)))

from math import hypot
n1 = float(input('Comprimento co cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa e equivalente a {:.2f}'.format(hypot(n1, n2)))

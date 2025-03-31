'''num = int(input('Digite um numero\n'
                'para calcular sei fatorial: '))
 
fatorial =  1



while num > 1 :
    fatorial *= num
    num -= 1


print(f'O fatorial de e {fatorial}')'''

# Acima está a minha resolução, abaixo a resolução proposta pelo professore.

from math import factorial
num =  int(input('Digite um número para ver seu fatorial: '))
fato = 1
c = num
print(f'Calculando o fatorial de {num}!', end= ' ')
while c > 0:
    print(f'{c}', end= ' ')
    print ('x' if c >1 else '=', end= ' ')
    fato *= c   
    c -= 1
print(f'{fato}')
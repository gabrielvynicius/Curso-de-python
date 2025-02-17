# Testando se forma um triangulo

'''print('\033[7;32;40m#__\033[m'* 20)
print('\033[1;36mIdentificando possibilidades de Triângulos\033[m')
print('\033[7;32;40m#__\033[m' * 20)
a = float(input('Digite o primeior comprimento da sua reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Seu triangulo e possivel')
else:
    print('Seu triangulo não e possivel ')

# Verificando qual tipo de triangulo e
if a == b == c:
    print('Seu triangulo e Equilátero')
elif a != b != c != a:
    print('Seu triangulo e Escaleno')
else:
    print('Seu triangulo e Isósceles')  

# End
# By Gabriel Vynicius'''

# Claramente o codigo acima esta correto, mas eu quero fazer de uma forma diferente.
# Vou colocar um if dentro do outro, para ver se consigo fazer de uma forma diferente.

print('\033[7;32;40m#__\033[m'* 20)
print('\033[1;36mIdentificando possibilidades de Triângulos\033[m')
print('\033[7;32;40m#__\033[m' * 20)

a = float(input('Digite o primeior comprimento da sua reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Seu triangulo e possivel')
    if a == b == c:
        print('Seu triangulo e Equilátero')
    elif a != b != c != a:
        print('Seu triangulo e Escaleno')
    else:
        print('Seu triangulo e Isósceles')
else:
    print('Seu triangulo não e possivel ')
# End
# By Gabriel Vynicius
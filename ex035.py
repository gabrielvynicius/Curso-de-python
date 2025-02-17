print('\033[7;32;40m#__\033[m'* 20)
print('\033[1;36mIdentificando possibilidades de Triângulos\033[m')
print('\033[7;32;40m#__\033[m' * 20)
a = float(input('Digite o primeior comprimento da sua reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Seu triangulo e possivel')
else:
    print('Seu triangulo não e possivel ')
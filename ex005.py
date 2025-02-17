# Colorindo o código.

fecha = '\033[m'
roxo = '\033[0;35;40m'
amarelo = '\033[0;33;40m'
azul= '\033[0;34;40m'
print('\n')
print(f'{roxo}={fecha}' * 90)

# Nesse cógido utiliza operaçôes aritimeticas para somar e subitrair, descobrindo a antecessor do numero e seu secessor.

a = int(input(f'{amarelo}Digite um número{fecha}{azul} '))
print(f'{amarelo}Sobre o número: {azul}{a}{fecha}')
print(f'{amarelo}Seu Antecessor é: {fecha}{azul}{a-1}')
print(f'{amarelo}Seu Sucessor é: {fecha}{azul}{a+1}')
print(f'{roxo}={fecha}' * 90)

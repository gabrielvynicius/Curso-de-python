# Colorindo o código!!

fecha = '\033[m'
branco = '\033[7;37;47m'
verde = '\033[7;32;42m'
marinho = '\033[0;36;40m'
roxo = '\033[0;35;40m'
verde2 = '\033[0;32;40m'
amarelo = '\033[0;33;40m'

print(f'{verde}={fecha}' * 90)
print('\n')                               

a = int(input('Digite um numéro: '))

print(f'{marinho}Calculando o dobro de {a} fica: {fecha}{amarelo}{a * 2}{fecha}')
print(f'{roxo}Seu triplo é: {fecha}{amarelo}{a * 3}{fecha}')    
print(f'{verde2}É sua raiz quadrada é:{ fecha}{amarelo} {a ** (1/2):.2f}{fecha}') 

print('\n')
print(f'{verde}={fecha}' * 90) 

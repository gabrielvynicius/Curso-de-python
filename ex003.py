# Primera tentativa de fazer o codigo

'''Soma1 = input('Digite um valor entre 10 e 15:')
Soma2 = input('Digite outro valor de 0 a 10:')
Resultado = Soma1 + Soma2
print('Somando esses valores vai dar exatamente: {} '.format(Resultado) )
"AQUI O RESULTADO CONCATENOU E O PROXIMO GODIGO FARA A SOMA UTILIZANDO O QUE FOI APRENDIDO A AULA DE NUMERO 6 " '''

# COLORINDO O CODIGO

fecha = '\033[m'
branco = '\033[0;30;40m'
vermelho ='\033[0;31;40m'
verde = '\033[0;32;40m'
amarelo = '\033[0;33;40m'
azul = '\033[0;34;40m'
roxo = '\033[0;35;40m]'
marinho = '\033[0;36;40'
cinza = '\033[0;37;40m'

# Depois de colocar todas as cores fiz o print de uma linha vazia para ficar mais orgaizado.

print('\n')
print(f'{verde}={fecha}'* 90)
numero1 = int(input(f'Digite o numero que você deseja somar sendo de 0 ao fintio até mesmo {vermelho} negativo {fecha}: '))
numero2 = int(input('Digite outro numero para que possamos efetuar a soma: '))
resultado = numero1 + numero2
mais100 = resultado + 100
print(f'O resultado da sua soma e equivalente á: {azul}{resultado}{fecha} e o mesmo somado 100 ficaria {azul}{mais100}{fecha}!!') 
print(f'{verde}={fecha}'* 90)
print('\n')

# Esse foi o exercicio 003 do curso em video, nele aprendemos como se soma dois numeros e como utilazar a INT para determinar uma variavel como um numeor inteiro.

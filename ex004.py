# Colorindo o Codigo.

fecha = '\033[m'
branco = '\033[0;30;40m'
vermelho = '\033[0;31;40m'
verde = '\033[0;32;40m'
amarelo = '\033[0;33;40m'
azul = '\033[0;34;40m'
roxo = '\033[0;35;40m'
marinho = '\033[0;36;40m'
cinza = '\033[0;37;40m'

# Utilizei um *def para criar uma função chamada traduzir nela faço a traducao e deixo em duas cores diferente para quando estiver falso ou verdadeiro.


def traduzir(valor):
    return f'{verde}Verdadeiro{fecha}' if valor else f'{vermelho}Falso{fecha}'


print('\n')
print(f'{marinho}={fecha}' * 90)

w = input('Digite algo para ser avaliado: ')
print(f'O tipo primitivo do que você digitou é:             : {verde}{type(w)}{fecha}')
print(f'O que foi digitado só tem {cinza}Espaços{fecha}:                  : {verde}{traduzir(w.isspace())}{fecha}')
print(f'O que foi digitado contem {azul}Apenas Números{fecha}:           : {verde}{traduzir(w.isnumeric())}{fecha}')
print(f'O que foi digitado {roxo}Alfanumérico{fecha}:                    : {verde}{traduzir(w.isalnum())}{fecha}')
print(f'O que foi digitado e somente {marinho}Alfabético{fecha}:            : {verde}{traduzir(w.isalpha())}{fecha}')
print(f'O qur foi digitado contem apenas letras {amarelo}Maiusculas{fecha}: : {verde}{traduzir(w.isupper())}{fecha}')
print(f'O que foi digitado contem apenas letras {branco}Minusculas{fecha}: : {verde}{traduzir(w.islower())}{fecha}')
print(f'O que foi digitado está {cinza}Capitalizado{fecha}:               : {verde}{traduzir(w.istitle())}')

print(f'{marinho}={fecha}' * 90)

# Os espaços no meio do código e para deixar mais organizado na hora de executar.

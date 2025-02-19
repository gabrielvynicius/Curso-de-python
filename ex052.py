# Colorindo o código
fecha = '\033[m'
amarelo = '\033[0;33;40m'
vermelho = '\033[0;31;40m'

num = int(input('Digite um número: '))  # Pedindo ao usuário para digitar um número.

# Verificando se é primo
if num > 1:
    total_divisores = 0  # Contador de quantas vezes `num` é divisível

    for c in range(1, num + 1):
        if num % c == 0:  # Se `num` for divisível por `c`
            total_divisores += 1
            print(f'{vermelho}{c}{fecha}', end=' ')  # Destaca os divisores em vermelho
        else:
            print(f'{amarelo}{c}{fecha}', end=' ')  # Números não divisores ficam amarelos

    print()  

    if total_divisores == 2:  # Se tiver apenas dois divisores (1 e ele mesmo)
        print('Seu número é primo!')
    else:
        print('Seu número NÃO é primo.')
else:
    print('Números menores ou iguais a 1 não são primos.')

print('Finalizado.')

# By Gabriel Vynicius.
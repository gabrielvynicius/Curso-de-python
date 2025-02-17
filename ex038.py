num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(f'O {num1} é {num1 - num2} vezes maior que {num2}.')
elif num2 > num1:
    print(f'O {num2} é {num2 - num1} vezes maior que {num1}.')
else:
    print('Não exinte diferenca de valores entres os dois números.')

print('=' * 30)
print('Sequencia de fibonacci')
print('-'*30)

n = int(input('Quantos termos você deseja mostrar: '))

n1 = 0
n2 = 1
cont = 1

print(n1 , end=' → ')

while cont < n :
    soma = n1 + n2
    print(n2, end=' → ')
    n1 = n2
    n2 = soma
    cont += 1
print('Fim')
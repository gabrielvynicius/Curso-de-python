a = int(input('Digite um numero : '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))
#maior
if a > b:
    if a > c:
        maior = a
    else:
        maior = c
else:
    if b > c:
        maior = b
    else:
        maior = c
#menor
if a < b:
    if a < c:
        menor = a
    else:
        menor = c
else:
    if b < c:
        menor =  b
    else:
        menor = c

print(f'O maior e o {maior}\n'
      f'O menor é o {menor}')

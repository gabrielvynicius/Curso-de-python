soma = 0
cont = 0 
for c in range (1,501,2):
    if c % 3 == 0:
        soma += c
        cont = cont + 1
print(f'Foram contados {cont} numeros e a soma entre os numeros e de {soma}')

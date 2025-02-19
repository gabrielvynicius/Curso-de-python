# Desenvolvendo um programa para ler 6 numeros e somar apenas os numeros pares.
s = 0
cont =  0
for c in range(1,7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
     s += num
     cont += + 1
print(f'A soma entre {cont} PARES é {s}')

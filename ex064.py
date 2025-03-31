soma =0
cont = 0
while True:
    n = int(input('Digite um numero [999 para parar.]: '))
    if n != 999:
        soma += n 
        cont += 1
    else:
        break
print(f'Você digitou {cont} números e a soma entre eles foi de {soma}.')

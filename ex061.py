print('Gerador de 10 PA')
print('-=' * 15)

num = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
vezes = 0

while vezes < 10:
    print(f'{num}', end=' → ')  
    num += razao  
    vezes += 1

print('FIM')  # Indica que a sequência terminou

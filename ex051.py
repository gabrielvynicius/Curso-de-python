print('=='*20)
print(' '*10,'10 TERMOS DE UMA PA')
print('=='*20)

termo =  int(input('Digite o Primeiro Termo: '))
razao = int(input('Razão: '))
decimo  = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    print(f'{c}', end=' → ')
print ('Finalizado.')

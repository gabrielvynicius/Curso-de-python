print('Gerador de PA')
print('==' * 10)

num = int(input('Digite um número para ver sua PA: '))
razao = int(input('Digite a razão: '))
vezes = 0
total_termos = 10  # Começamos com 10 termos
cont = 1  # Qualquer valor diferente de 0 para entrar no loop

# Gerando os primeiros 10 termos
while vezes < 10:
    print(f'{num}', end=' → ')
    num += razao
    vezes += 1
print('PAUSA')

# Perguntar quantos termos mais o usuário quer ver
while cont != 0:
    cont = int(input('Quantos termos você quer mostrar mais? '))
    total_termos += cont  # Atualiza o total de termos

    # Gerando os novos termos pedidos
    for _ in range(cont):
        print(f'{num}', end=' → ')
        num += razao
    
    print('PAUSA')

print(f'Progressão finalizada com {total_termos} termos mostrados.')

print('=' * 49)
primeiro_num = int(input('Digite um Número: '))
print('=' * 15,'Base de Conversão','=' * 15)
print('=' * 49)
print('Digite 1 para Binario.')
print('Digite 2 para Octal.')
print('Digite 3 para Hexadecimal.')
print('=' * 49)

while True:

    num = primeiro_num
    usadas = set()

    while usadas != {'1','2','3'}:
        
        base = input('Digite a base de conversão: ')
        
        if base == '1' and '2' not in usadas:
            print(f' Seu número em Binario é: {bin(num)[2:]}') 
            usadas.add('1')
        elif base == '2' and '2' not in usadas:
            print(f' Seu número em Octal é: {oct(num)[2:]}')
            usadas.add('2')
        elif base == '3' and '3' not in usadas:
            print(f'Seu número em hexadecimal é: {hex(num)[2:]}')
            usadas.add('3')
        else:
            print('Opção invalida ou já utilizada!')
    
    print('=' * 49)
    print(f'Você ja utilizou todas as conversões! O primeiro número digitado foi: {primeiro_num} ')
    print('=' * 49)

    novo_num = input('Deseja inserir um novo número? ').strip().lower()
    if novo_num == 'sim':
        primeiro_num = int(input('Digite um número: '))
    else:
        print('Obrigado por utilizar o programa! ')
        break
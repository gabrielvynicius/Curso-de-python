maior = 0

while True:
    n = int(input('Primeiro valor: '))
    nn = int(input('Segundo valor: '))

    while True:  # Mantém o menu ativo até que o usuário escolha trocar os números ou sair
        print('''\n[1] Soma
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa ''') 
        
        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            print(f'A soma entre {n} + {nn} é {n + nn}')
        elif opcao == 2:
            print(f'A multiplicação entre {n} x {nn} é {n * nn}')
        elif opcao == 3:
            maior = max(n, nn)
            print(f'O maior número entre {n} e {nn} é {maior}.')
        elif opcao == 4:
            break  # Volta para pedir novos números
        elif opcao == 5:
            print('Finalizando o programa...')
            exit()  # Encerra o programa
        else:
            print('Opção inválida! Tente novamente.')

while True:   
    print('=-' * 40)
    n = int(input('Primeiro valor: '))
    nn = int(input('Segundo valor: '))

    maior = 0


    while True: 
        print(('=-'* 40))
        print('''[1] Soma
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa ''')
        if n> nn: 
            maior = n
        else:
            maior = nn

        opcao = int(input('Digite uma opcão: '))  
        if opcao == 1:
            print(f'A soma entre {n} + {nn} é {n + nn}')
        elif opcao == 2:
            print(f'A multiplicação entre {n} x {nn} é {n * nn} ')
        elif opcao == 3:
            print(f'Entre o numero {n} e {nn} o número maior e o {maior}.')
        elif opcao == 4:
            break
        elif opcao == 5:
            print('Finalizando programa')
            exit()
        else:
            print('Opção invalida, tente novamente.')
salario = float(input('Quanto você ganha ao mês: '))
if  salario > 1250.0:
    print(f'Seu salario teve um reajuste de 10% então agora voce vai passar a receber R${ salario+ (salario * 0.10)}')
else:
    print(f'Seu salario teve um reajuste de 15% então você agora vai passar a receber R$ {salario + (salario * 0.15)}')
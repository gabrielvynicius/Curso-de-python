# Colorindo o codigo.

fecha = '\033[m'
verde = '\033[0;32;40m'
vermelho = '\033[0;31;40m'


casa = float(input('Qual e o valor do Imovel? R$ '))
salario = float(input('Qual e a sua media salarial? R$ '))
anos = int(input('Em quantos anos você deseja pagar: '))


if casa / (anos * 12) < salario * (30/100):
    print(f'O valor da parcela sera de R$ {casa / (anos * 12):.2f}')
    print(f'Seu emprestimo foi {verde}Aprovado')
else:
    print(f'Seu emprestimo foi {vermelho}Negado')

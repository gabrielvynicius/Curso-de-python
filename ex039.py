#'''ano = int(input('Digite o ano de seu nacimento: '))
#mês = int(input('Digite o mês de 1 a 12: '))
#dia = int(input('Digite o dia de 1 a 31: '))

#print (f'Voce naceu em {dia}/{mês}/{ano}.')

#if 2025 - ano !=0 and 2025 - ano < 18 :
#    print(f'Falta {abs((2025 - ano) - 18)} para você se alistar.')
#elif (2025 - ano) - 18 == 0:
#    print(f'Esse ano você precisa se alistar seu safado, vai capinar um lote.')
#elif 2025 - ano > 18:
 #   print(f'já passou {(2025 - ano) - 18} anos 1 dia e 2 mêses.')'''

#acima foi minha tentativa de fazer o exercicio, abaixo a resolução do curso.

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')

#OBS: O exercicio foi feito com a data atual, então se você for fazer o exercicio em 2025, terá que mudar a data atual para 2025.

#by: Gabriel Vynicius 

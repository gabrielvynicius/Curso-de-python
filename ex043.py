# Desenvolvendo logica para calcular o IMC de uma pessoa
# IMC = Peso / Altura ** 2
# Abaixo de 18.5: Abaixo do pesoa
# Entre 18.5 e 25: Peso ideal
# 25 ate 30: Sobrepeso
# 30 ate 40: Obesidade
# Acima de 40: Obesidade mórbida
# By Gabriel Vynicius


print('\033[7;32;40m#__\033[m'* 20)
print('\033[1;36mCalculando o IMC de uma pessoa\033[m')
print('\033[7;32;40m#__\033[m' * 20)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu IMC e de {imc:.2f} e você esta abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Seu IMC e de {imc:.2f} e você esta no peso ideal')
elif 25 <= imc < 30:
    print(f'Seu IMC e de {imc:.2f} e você esta com sobrepeso')
elif 30 <= imc < 40:
    print(f'Seu IMC e de {imc:.2f} e você esta com obesidade')
else:
    print(f'Seu IMC e de {imc:.2f} e você esta com obesidade mórbida')

# End
# By Gabriel Vynicius
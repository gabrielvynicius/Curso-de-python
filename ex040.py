'''nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media <= 4.99:
    print(f'Aluno reprovado com a media {media}')
elif 5 <= media <7:
    print(f'O aluno ficou de recuperção com a media {media}')
else:
    print(f'O aluno foi aprovado com a nota {media}')'''

#versão colorida

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media <= 4.99:
    print(f'\033[31mAluno reprovado com a media {media}\033[m')
elif 5 <= media <7:
    print(f'\033[33mO aluno ficou de recuperção com a media {media}\033[m')
else:
    print(f'\033[32mO aluno foi aprovado com a nota {media}\033[m')

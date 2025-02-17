from math import sin, cos, tan, radians
n1 = int(input('Digite o ângulo qua você deseja: '))
print('O ângulo de {} tem o SENO de {:.2f}\n'
      'O ângulo de {} tem o COSSENO de {:.2f}\n'
      'O ângulo de {} tem o TANGENTE de {:.2f}\n'
      .format(n1, sin(radians(n1)), n1, cos(radians(n1)), n1, tan(radians(n1))))

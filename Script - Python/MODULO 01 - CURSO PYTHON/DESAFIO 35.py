n = int(input('Escreva o primeiro número: '))
n1 = int(input('Agora o segundo: '))
n2 = int(input('O último: '))

if n > n1 > n2:
   print('O maior é {}'.format(n))
   print('O menor é {}'.format(n2))
elif n > n2 > n1:
    print('O maior é {}'.format(n))
    print('O menor é {}'.format(n1))
elif n1 > n2 > n:
    print('O maior é {}'.format(n1))
    print('O menor é {}'.format(n))
elif n1 > n > n2:
    print('O maior é {}'.format(n1))
    print('O menor é {}'.format(n2))
elif n2 > n > n1:
    print('O maior é {}'.format(n2))
    print('O menor é {}'.format(n1))
elif n2 > n1 > n:
    print('O maior é {}'.format(n2))
    print('O menor é {}'.format(n))
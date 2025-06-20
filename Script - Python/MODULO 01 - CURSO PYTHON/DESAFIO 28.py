f  =  input('Escreva uma frase: ')
f1  =  f.upper()
f2  = f1.count('A')
f3  = f.find('A')
f4  = f.rfind('A')
print('A quantidade de A foram {}'.format(f2))
print('A posição que apareceu A na primeira vez foi {}'.format(f3+1))
print('Já a última vez do A foi {}'.format(f4+1))

# O motivo de ter +1 é pelo caractere começar pelo zero, então acrescenta mais um número
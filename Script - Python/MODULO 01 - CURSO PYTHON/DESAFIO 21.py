import random
print ('---------SORTEIO--------')
p = str(input('Digite do primeiro aluno: '))
p1 = str(input('O segundo: '))
p2 = str(input('O terceiro: '))
p3 = str(input('E o último: '))
s = (p, p1, p2, p3)
s1 = random.choice(s)
print('Será {}'.format(s1))
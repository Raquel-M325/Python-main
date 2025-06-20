import random
p = str(input('Digite o primeiro nome do aluno: '))
p1 = str(input('O segundo: '))
p2 = str(input('O terceiro: '))
p3 = str(input('O quarto: '))
r = (p,p1,p2,p3)
o = random.sample(r,k=4)
print('Respectivamente, de primeira posição até o último foram: {}'.format(o))

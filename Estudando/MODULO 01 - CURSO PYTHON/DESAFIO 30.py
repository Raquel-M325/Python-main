from random import randint
from time import sleep

c = randint(0, 5)
p = int(input('Tente descobrir qual número eu escolhi, entre 0 a 5, digite: '))
print('PROCESSANDO...')
sleep(3)
if p  == c:
    print('VENCEU, PARABÉNS!')
else:
    print('Que pena, pensei em {}, não o {}'.format(c,p))






#p = int(input('Tente descobrir qual número eu escolhi, entre 0 a 5, digite: '))
#if p == 4:
#   print('VENCEU, PARABÉNS!')
#else:
#   print('PERDEU! Tente na próxima vez!')

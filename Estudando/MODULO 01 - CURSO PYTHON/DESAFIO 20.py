import math
n = (float(input('Digite o ângulo: ')))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
s = math.sin(math.radians(n))
print('O cos é {:.2f}, o tg {:.2f} e sen {:.2f}'.format(c,t,s))
# Precisa converter os radianos! Use mais o math
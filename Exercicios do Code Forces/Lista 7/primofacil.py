n = int(input())
qdivisores = 0
m = int(n ** (1/2))
for i in range(1,m+1):
    m1 = n % i
    if m1 == 0:
        qdivisores = (i)
if qdivisores > 2:
    print('Nao')
else:   
    if n < 2:
        print('Nao')
    elif n == 2:
        print('Sim')
    elif n % 2 == 0:
        print('Nao')
    else:
        print('Sim')
x, y = map(float,input().split())

if y > 0 and x > 0:
    print('Q1')

elif x < 0 and y > 0:
    print('Q2')

elif  y < 0 and x < 0:
    print('Q3')

elif  x > 0 and y < 0:
    print('Q4')

elif x == 0 and y == 0:
    print ('Origem')

elif y == 0:
    print ('Eixo X')

elif x == 0:
    print ('Eixo Y')
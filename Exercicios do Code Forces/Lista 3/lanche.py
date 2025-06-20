c, q = map(int,input().split())

if c == 1:
    c = 4
    t = float(c * q)
    print('Total: R$ {:.2f}'.format(t))

elif c == 2:
    c = 4.5
    t = float(c * q)
    print ('Total: R$ {:.2f}'.format(t))

elif c == 3:
    c = 5
    t = float(c * q)
    print ('Total: R$ {:.2f}'.format(t))

elif c == 4:
    c = 2
    t = float(c * q)
    print ('Total: R$ {:.2f}'.format(t))

elif c == 5:
    c = 1.5
    t = float(c * q)
    print ('Total: R$ {:.2f}'.format(t))
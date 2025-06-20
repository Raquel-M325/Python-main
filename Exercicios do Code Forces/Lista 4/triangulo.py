a, b, c, d = map(int,input().split())
if (a + b > c) and (a + c > b) and (b + c > a):
    print ('s')
elif (a + b > d) and (a + d > b) and (b + d > a):
    print ('s')
elif (a + c > d) and (a + d > c) and (c + d > a):
    print ('s')
elif (b + c > d) and (b + d > c) and (c + d > b):
    print ('s')
else:
    print ('n')
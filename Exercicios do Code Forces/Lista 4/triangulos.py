a, b, c = map(int,input().split())
if (a + b <= c) or (b + c <= a) or (c + a <= b): 
    print ('n')
else:
    if a > b and a > c :
        if (c**2 + b**2 > a**2):
            print ('a')
        elif (c**2 + b**2 < a**2):
            print ('o')
        elif (c**2 + b**2 == a**2):
            print('r')
 
    elif b > a and b > c :
        if (c**2 + a**2 > b**2):
            print ('a')
        elif (c**2 + a**2 < b**2):
            print ('o')
        elif (c**2 + a**2 == b**2):
            print('r')
        
    elif c > a and c > b:
        if (b**2 + a**2 > c**2):
            print ('a')
        elif (b**2 + a**2 < c**2):
            print ('o')
        elif (b**2 + a**2 == c**2):
            print('r')
    elif a == b == c:
        if (a**2 + b**2 > c**2):
            print ('a')
        elif (a**2 + b**2 < c**2):
            print ('o')
        elif (a**2 + b**2 == c**2):
            print('r')
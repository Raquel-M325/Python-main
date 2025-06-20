a,b,c = map(float,input().split())
 
if a + b == c or a + c == b or b + c == a or a == b or b == c or a == c or a == b == c:
    print('S')

elif a + b != c or a + c != b or b + c != a or a != b != c:
    print('N')
a = int(input())
b = int(input())    
c = int(input())
d = int(input())
e = int(input())

maior = a
 
if a > b and a > c and a > d and a > e:
    print(a)
elif b > a and b > c and b > d and b > e:
    print(b)
elif c > a and c > b and c > d and c > e:
    print(c)
elif d > a and d > b and d > c and d > e:
    print(d)  
elif e > a and e > b and e > c and e > d:
    print(e) 
elif maior > b:
    print (a)
elif maior > c:
    print (a)
elif maior > d:
    print (a)
elif maior > e:
    print (a)
elif maior < b:
    print (b)
elif maior < c:
    print (c)
elif maior < d:
    print (d)
elif maior < e:
    print (e)
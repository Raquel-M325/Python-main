n1, d1, v1 = map(int,input().split())
n2, d2, v2 = map(int,input().split())

km1 = d1/1000
km2 = d2/1000

t1 = km1/v1
t2 = km2/v2

if t1 > t2:
    print(n2)
else:
    print(n1)
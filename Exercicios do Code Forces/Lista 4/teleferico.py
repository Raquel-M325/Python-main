c = int(input())
a = int(input())
 
c1 = c - 1
t = a // c1

if a % c1 != 0:
    v = t + 1
    print(v)
else:
    print(t)

a11, a21 = map (int,input().split())
a12, a22 = map (int, input().split())
p1, p2 = map (int, input().split())

pt = p1 + p2

m1 = a11 * p1 + a21 * p2
r1 = m1 // pt

m2 = a12 * p1 + a22  * p2
r2 = m2 // pt

if r1 > r2:
    print (1)
elif r1 < r2:
    print (2)
elif r1 == r2:
    print(1)
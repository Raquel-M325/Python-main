b = int (input())
t = int (input())

m1 = 160 - b
m2 = 160 - t
m = m1 * m2
f = b * t

if m == f:
    print("0")
elif m < f:
    print("1")
elif m > f:
    print("2")
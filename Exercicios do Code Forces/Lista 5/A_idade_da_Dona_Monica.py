m = int(input())
a = int(input())
b = int(input())

s = a + b
i = m - s

if (i > b) and (i > a):
    print(i)
elif (a > b) and (a > i):
    print(a)
elif (b > a) and (b > i):
    print(b)
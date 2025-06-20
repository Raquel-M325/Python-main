n = int(input())
 
if n <= 10:
    print(7)
elif n >= 11 and n <= 30:
    r = n-10
    r1 = r*1
    t = r1 + 7
    print(t)
elif n >= 31 and n <= 100:
    r = n-30
    r1 = r*2
    t = r1 + 7 + 20 
    print(t)
elif n >= 101:
    r = n-100
    r1 = r * 5
    rt = r1 + 7 + 20 + 140
    print(rt)
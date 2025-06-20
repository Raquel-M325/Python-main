a, g, ra, rg = map(float,input().split())
r1 = (a / ra)
r2 = (g / rg)
if r1 < r2:
    print ('A')
else:
    print ('G')
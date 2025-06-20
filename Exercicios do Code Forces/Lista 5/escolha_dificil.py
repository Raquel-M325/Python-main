ca, ba, pa =  map(int,input().split())
cr, br, pr =  map(int,input().split())

r1 = cr - ca
r2 = br - ba
r3 = pr - pa

if r1 < 0:
    r1 = 0
if r2 < 0:
    r2 = 0
if r3 < 0:
    r3 = 0

t = r1 + r2 + r3
print(t)
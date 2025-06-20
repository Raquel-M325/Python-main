a = int(input())
b = int(input())
c = int(input())
d = int(input())

n1 = a + d
n2 = b + c
n3 = a + b
n4 = d + c


if n1 > n3:
    maior = n1
else:
    maior = n3
if n2 < n4:
    menor = n2
else:
    menor = n4
if maior > menor:
    r = maior - menor
else:
    r = menor - maior

print (r)
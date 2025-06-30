n = int(input())
n1 = list(map(int, input().split()))
m = sum(n1) / n
i1 = 0
i2 = 0
print('{:.1f}'.format(m))
for i in range(0,n):
    if n1[i] >= m:
        i2 = i2 + 1 
    else:
        i1 = i1 + 1
print(i1)
print(i2)
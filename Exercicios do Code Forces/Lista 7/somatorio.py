n = int(input())
p = 0
for i in range (0,n):  
    p = p + 1/(i+1)
print ('{:.4f}'.format(p))
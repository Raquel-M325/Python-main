
n = int(input())
p1 = n // 100
p2 = (n - p1 * 100) // 50  
r3 = (n - p1 * 100) - (p2 * 50) 
p3 = r3 // 20
r4 = (n - p1 * 100) - (p2 * 50) - (p3 * 20)
p4 = r4 // 10
r5 = (n - p1 * 100) - (p2 * 50) - (p3 * 20) - (p4 * 10) 
p5 = r5// 5
r6 = (n - p1 * 100) - (p2 * 50) - (p3 * 20) - (p4 * 10) - (p5 * 5)
p6 = r6// 2
r7 = (n - p1 * 100) - (p2 * 50) - (p3 * 20) - (p4 * 10) - (p5 * 5) - (p6 * 2)
p7 = r7// 1
print (n)
print ('{} nota(s) de R$ 100,00'.format(p1))
print ('{} nota(s) de R$ 50,00'.format(p2))
print ('{} nota(s) de R$ 20,00'.format(p3))
print ('{} nota(s) de R$ 10,00'.format(p4))
print ('{} nota(s) de R$ 5,00'.format(p5))
print ('{} nota(s) de R$ 2,00'.format(p6))
print ('{} nota(s) de R$ 1,00'.format(p7))
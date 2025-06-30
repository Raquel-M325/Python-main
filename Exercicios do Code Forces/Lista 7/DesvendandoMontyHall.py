n = int(input())
vitorias = 0 
for i in range(n):
    porta = int(input())
    if porta == 2 or porta == 3:
        vitorias += 1
print(vitorias)
n = int(input())
soma = 0
numanterior = None
for i in range(n):
    v = int(input())
    if numanterior is None:
        soma = 1
    elif v != numanterior:
        soma += 1
    numanterior = v
print(soma)


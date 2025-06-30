c = int(input())
saldo = 100
maior = saldo
for i in range(c):
    novovalor = int(input())
    saldo = saldo + novovalor
    if saldo > maior:
        maior = saldo
print(maior)
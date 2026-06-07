n  = int(input('Digite um número: '))
n1 = n // 1 % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 % 10
print('Unidade: {}'.format(n1))
print('Dezena: {}'.format(n2))
print('Centena: {}'.format(n3))
print('Milhar: {}'.format(n4))

# Ambos estão certos, mas não é tão vantajoso de baixo em comparação de cima, mas veja os dois!
# Além disso, cuidado em utilizar :.0f por arredondar os números e use dois divisores para diminuir os zeros!

#n = (input('Digite um número de 0 a 9999 somente: '))
#n1 = n[3]
#n2 = n[2]
#n3 = n[1]
#n4 = n[0]
#v1 = n.
#print('Unidade: {}'.format(n1 - ))
#print('Dezena: {}'.format(n2))
#print('Centena: {}'.format(n3))
#print('Milhar: {}'.format(n4))


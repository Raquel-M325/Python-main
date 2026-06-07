d = float(input('Quantos dias utilizou o carro? '))
km = float(input('E quantos Km você percorreu? '))
p1 = d * 60
p2 = km * 0.15
print('Você terá que pagar {} R$'.format(p1+p2))
# Carro custa 60 R$ por dia e 0,15 R$ por Km
# Não use vírgula nos valores!
from math import hypot
co  = float(input('Digite o comprimento do cateto adjacente: '))
ca  = float(input('Agora do cateto oposto, o comprimento: '))
h = hypot(co,ca)
print('A hipotenusa é {:.2f}'.format(h))
# :.2f conta em duas casas decimais, mas se quiser mais ou menos, pode mudar o 2 pelo o que você quer
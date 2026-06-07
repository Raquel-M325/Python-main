v = float(input('Digite o Km que você fará a viagem: '))
if v <= 200:
    v1 = 0.50 * v
    print('Você terá que pagar de {} reais'.format(v1))
else:
    v2 = (v - 200) * 0.45
    print('Você terá que pagar de {} reais'.format(v2))

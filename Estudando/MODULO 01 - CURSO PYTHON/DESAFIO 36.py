s = float(input('Digite o valor do seu salário: '))
if s <= 1250:
    s1 = (s * 15/100) + s
    print('O seu aumento será de {} reais'.format(s1))
else:
    s2 = (s * 10/100) + s
    print('O seu aumento foi de {} reais'.format(s2))
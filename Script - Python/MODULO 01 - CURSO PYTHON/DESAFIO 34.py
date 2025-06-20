a = int(input('Digite aqui o ano: '))
if a % 4 == 0 and (a % 400 == 0 or a % 100 != 0):
    print('É ano bissexto')
else:
    print('Não é ano bissexto')
# Teve que seguir pelo sentido da regra do bissexto!
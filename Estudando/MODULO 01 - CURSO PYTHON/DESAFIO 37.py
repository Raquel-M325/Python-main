t = float(input('Digite o comprimento da primeira reta: '))
t1 = float(input('Agora da segunda reta: '))
t2 =  float(input('A última reta: '))

if t == t1 == t2:
    print('É triângulo equilátero')
elif t == t1 or t1 == t2 or t == t2:
    print('É triângulo isósceles')
elif t + t1 <= t2:
    print('Não é triângulo')
elif t != t1 and t1 != t2 and t != t2:
    print('É triângiulo escaleno')
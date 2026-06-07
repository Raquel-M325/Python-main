n1 = float(input('Qual é a porcentagem do valor? '))
n2 = float(input('E qual é o valor? '))
a =  n2 * (n1/100)
r = n2 + a
print('O novo valor é {}R$ de {}%, ou seja, ganhando {}R$ mensalmente.'.format(r,n1,r-n2))
a1 = (n1/100) * 12
r1 = n2 * a1
r2 = r1 + n2
print('Agora, em ano é {}R$ de juros, ou seja, com a capital é {}R$ durante 12 meses'.format(r1,r2))
t = float(input('Que ano estamos? '))
t1 = float(input('Qual ano que começou? '))
t2 = t - t1
rf = t2 * r1
print('O resultado total foi {}R$ de juros, durante {} anos, ou seja, com a capital, você tem {}R$'.format(rf,t2, rf + n2))
# Isso é exemplo de juros simples! 
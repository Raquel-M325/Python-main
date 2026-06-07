n  =  input('Digite o seu nome completo: ')
n1 =  n.split()
print('Primeiro nome: {}'.format((n1 [0])))
print('O último nome: {}'.format(n1 [-1]))
# O motivo de -1 é porque você está colocando o final da lista, se colocar +1, vai entender que é além do que está escrito,
# ou seja, não existe, por isso que python sempre conta -1 nos caracteres para evitar esse problema
# Resumindo, -1 indica o último!
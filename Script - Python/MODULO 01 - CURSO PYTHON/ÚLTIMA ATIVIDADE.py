#Vamos fazer primeiro o dicionário

cores = {'limpa':'\033[30m',
         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:37:47m'}
n = str(input('Olá! Digite o seu nome: '))
print('Seja bem vindo, {}{}{}'.format(cores['amarelo'],n, cores['azul']))

#a útima cor escrita é mais se quiser colocar outra cor como marca texto,
# mas acabei não querendo por achar pouco estranho o design
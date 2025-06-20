a1 = input('Digite algo: ')
print('Qual é o tipo?', type(a1))
print('É número?', a1.isnumeric(),)
print ('É letra?', a1.isalpha())
print('É decimal?',a1.isdecimal())
print('Tem espaço?', a1.isspace())
print('É alfanúmerico?', a1.isalnum())

# Se lembre sempre de "usar o ponto" para interligar com o valor de cima!
# Inclusive com ".format", se esquecer, não irá funcionar.
# Seja em qualquer comando, ele não consegue ler como "true"...
# ... com a digitação com espaço, ou seja, sempre será false.
# Alpha é letra, numeric é número, dois juntos lerão os dois.
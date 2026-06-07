n1 = float(input('Qual quantidade de metros quer que eu calcule? '))
print ('Em centímetros é {} cm, em milímetros é {} mm, dos {} metros'.format(n1*100, n1*1000, n1))
# Lembre que cada medida, se conta de si mesmo para outro, aumentando/descrescendo 0
# Por exemplo: 1m em mm ---> 1000 mm (m,cm,mm)
# 1cm em m ---> 0,01 m (cm, m)
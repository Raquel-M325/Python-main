def dia_da_semana(h,d):
    nomedodia = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
    indicedehoje = nomedodia.index(h)
    indicedoevento = (indicedehoje + d) % 7
    return nomedodia[indicedoevento] 

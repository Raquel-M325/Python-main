def dia(dia, mes, ano):
    nomedomes = ['janeiro','fevereiro','marco','abril', 'maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    diafinal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes > 12 or mes < 1:
        return 'Data Invalida'
    if dia < 1 or dia > diafinal[mes - 1]:
        return 'Data Invalida'
    if ano < -10000 or ano > 10000:
        return 'Data Invalida' 
    diaformatado = f'{dia:02d}'
    return f'{diaformatado} de {nomedomes[mes - 1]} de {ano}'






def soma(valores):
    """soma realiza a soma dos valores que estão em uma lista e retorna resultado da soma"""
    rs = 0
    for i in valores:
        rs += i 
    return rs
def media(valores):
    """media realiza a soma dos valores que estão em uma lista e divide pela quantidade dos valores somados e retorna o resultado"""
    rs = 0 
    qtd = len(valores)
    for i in valores:
        rs += 1
        return rs/qtd
def maior(valores):
    """maior retorna o maior valor de uma lista"""
    m = valores[0]
    for i in valores:
        if i > m :
            m = i 
    return m
def menor(valores):
    """menor retorna o menor valor de uma lista"""
    m = valores [0]
    for i in valores:
        if i < m:
            m = i
    return m 
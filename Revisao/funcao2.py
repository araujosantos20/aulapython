def soma(lista):
    rs = 0
    for i in lista:
        rs+=i
    return rs


def maior(lista):
    m = lista[0]
    for i in lista:
        if i > m:
            m = i
    return m
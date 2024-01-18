def soma(num):
    """a funçao realiza a soma dos números que são passados por parametro e ao final retorna o resulad da soma
       obs: você deve passar por parâmetro de uma lista com números"""
    result = 0
    for i in num:
        result += i
    return result

v = [10,1]
print(soma(v))
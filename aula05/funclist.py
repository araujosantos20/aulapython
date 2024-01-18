import os 
os.system("clear")

lista = [2, 4, 6, 8]
dic = {
    "1":10,
    "2":20,
    "3":30
}
def soma(valores):
    rs = 0
    for i in valores:
        rs += i 
    print(rs)

def soma2(*valores):
    a, b, c, d = valores
    rs = a+b+c+d 
    print(rs)

def soma3(**num):
    a,b,c = num
    rs = num[a]+num[b]+num[c] 
    print(rs)

soma(lista)
soma2(*lista)
soma3(**dic)


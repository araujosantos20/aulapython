# import ctypes

# func = ctypes.CDLL("./saida.so")
# func.limpar()


import os 
cores = ["azul", "verde", "rosa", "lilás", "preto", "branco", "roxo", "amarelo"]
os.system("clear")
#print(cores[5])
#para exibição de um elemento específico

# for c in cores:
#     print("Eu gosto de " +c)

# exibição de todos os elemntos 

q = 1

for c in cores:
    print(str(q)+"ª cor é "+c)
    q = q + 1
import os 
os.system("clear")

arq = open("./arquivos/info.csv", "r")
print(arq.read())
arq.close()
import os 
os.system("clear")

arq = open("./arquivos/dados.csv", "a")

nome = input("digite o seu nome: ")
mail = input("digite o seu e-mail: ")

arq.write(nome+";"+mail+"\n")

arq.close()
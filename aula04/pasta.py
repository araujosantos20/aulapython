import os 

os.system("clear")
os.system("rm -r dadosINFO")
os.mkdir("dadosINFO") #cria um diretório
os.chdir("dadosINFO") #abre o diretório
ar = open("text.txt", "x") #cria um arquivo de texto
ar.write("texto") #insere um texto no arquivo de texto
ar.close()
os.getcwd()
print(os.getcwd())
print("diretório criado")
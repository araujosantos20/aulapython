import os

os.system("cls")
print("Temos dois arquivos: bloco_texto.txt e dados.txt")
print("Qual deles você deseja apagar?")
es = input("Digite: \n - 1 para bloco_texto\n - 2 para dados.txt\n: ")

if es == "1":
    es = input("Você tem certeza que deseja apagar o arquivo?\n [s,n]:")
    if es == "s":
        os.remove("bloco_texto.txt")
        print("Arquivo excluído com sucesso!")
else:
    es = input("Você tem certeza que deseja apagar o arquivo?\n [s,n]")
    if es == "s":
        os.remove("dados.txt")
        print("Arquivo excluído com sucesso!")
import os

os.system("cls")

fl = open("dados.txt", "a")
texto = input("Digite algo: ")
fl.write(texto+"\n")
fl.close()
rs = input ("Você deseja renomear o arquivo?[s,n]: ")
if rs == "s":
    novo_nome=input("Digite o novo nome do arquivo: ")
    os.rename("dados.txt",novo_nome)
    print("O arquivo foi renomeado com sucesso")
else:
    print("Veja o resultado")
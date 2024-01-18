# Este programa obtém o nome do aluno e a nota média
# Se o aluno tiver uma média acima ou igual a 6
# Estará aprovado, caso contrário, reprovado

nome = input("Digite o nome do aluno: ")
media = input("Digite a nota média do aluno: ")
media = float(media)

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
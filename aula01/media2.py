import ctypes

func = ctypes.CDLL("./saida.so")
func.limpar()

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aluno está aprovado")
elif nota <= 4:
    print("Aluno reprovado")
else: 
    print("Aluno de recuperação")
    trab = float(input("Digite a nota do trabalho de recuperação: "))
    if trab > 6:
        print("Aluno foi aprovado")
    else:
        print("A nota não foi suficiente. Aluno foi reprovado")

# Este programa realiza as 4 operações matemáticas
n1 = input("Digite um número: ")
n2 = input("Digite um número: ")
# print(type(n1))
n1 = int(n1)
n2 = int(n2)
# print(type(n1))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print("O resultado da soma é: "+str(soma))
print("O resultado da subtração é: "+str(subtracao))
print("O resultado da multiplicação é: "+str(multiplicacao))
print("O resultado da divisão é: "+str(divisao))

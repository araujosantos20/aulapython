#!/usr/bin/python3 

nome = input("Digite o seu nome: ")
nasc = input("Digite o ano do seu nascimento: ")
#para realizar o cálculo da idade, foi necessário converter a variável nasc para 
#inteiro, pois o comando input sempre retorna o valor como texto
idade = 2023 - int(nasc)
#para converter a idade em inteiro,  usamos o comando str

print("Ola sr(a)."+nome+". A sua idade este ano é ou será de "+str(idade)+" anos")
from class_cliente import Cliente

nome = input("Digite o nome do cliente: ")
email = input("Digite o email do cliente: ")
cpf = input("Digite o cpf do cliente: ")
idade = int(input("Digite a idade do cliente: "))
telefone = input("Digite o telefone do cliente: (11)")

# Vamos instanciar a classe Cliente. Gerar um objeto
# a partir da classe Cliente passando todas as 
# propriedades para o objeto criado

cli = Cliente()
cli.gravarCliente(nome, email, cpf, idade, telefone)




import os
class Cliente:
    def __init__(self):
        self.__nome = ""
        self.__email = ""
        self.__cpf = ""
        self.__idade = 0
        self.__telefone = ""
    def gravarCliente(self, nome="", email="", cpf="", idade=0, telefone=""):
        
        if (nome=="" 
            or email=="" 
            or cpf=="" 
            or idade < 18 
            or telefone == "" 
            or not cpf.isnumeric() 
            or len(cpf) != 11
            or len(telefone) != 9
            or email.find("@")):
            print("DIGITE TODOS OS CAMPOS CORRETAMENTE!")
        else:    
            self.__nome = nome
            self.__email = email
            self.__cpf = cpf
            self.__idade = idade
            self.__telefone = telefone
            self.__gravar()
    def __gravar(self):
        
        arquivo = open("dados/infocliente.csv","a")
        arquivo.write("Nome: {};\n".format(self.__nome))
        arquivo.write("E-mail: {};\n".format(self.__email))
        arquivo.write("CPF: {};\n".format(self.__cpf))
        arquivo.write("Idade: {};\n".format(str(self.__idade)))
        arquivo.write("Telefone: {};\n".format(self.__telefone))
        arquivo.close()
        print("Cliente gravado com sucesso")
        
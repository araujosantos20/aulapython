import os
os.system("clear")

class User:
    def __init__(self, nomeUser, senha, nivelAcesso):
        self.nomeUser = nomeUser
        self.senha = senha
        self.nivelAcesso = nivelAcesso

    def login(self, nomeUser, senha):
        if self.nomeUser == nomeUser and self.senha == senha:
            print("Você está logado\nSeja bem-vindo!")
        else:
            print("Nome de usuário ou senha incorreto")
    def alterarSenha(self, nomeUser, novaSenha):
        if self.nomeUser == nomeUser:
            self.senha = novaSenha
            print("senha alterada")
        else:
            print("usuário inexistente")
    def logout(self):
        self.nomeUser = ""
        self.senha = ""
        self.nivelAcesso = ""
        print("Você saiu do sistema")
class Usuario:
    def __init__(self):
        self.__nomeusuario = ""
        self.__senha = ""
        self.__email = ""
        self.__nivelacesso = ""
    def setData(self, nomeusuario, senha, email, nivelacesso):
        self.__nomeusuario = nomeusuario
        self.__senha = senha
        self.__email = email
        self.__nivelacesso = nivelacesso
    def authenticated(self):
        print()
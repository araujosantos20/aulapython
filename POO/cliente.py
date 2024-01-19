# Declaração de classe Cliente. Esta classe permite
# que seja criados novos objetos do tipo cliente
class Cliente:
    # A implementação do método __init__ representa a construção
    # do método contrutor da classe, responsável por inicializar
    # o objeto que será criado. Este método possui um argumento
    # self que faz refêrencia a própria classe. Quando for
    # criar um método de classe deve-se utilizar o comando
    # self para referênciar a própria estrutura de classe a qual
    # ele pertence.
    # Note que o método __init__(construtor) foram iniciados os
    # atributos da classe, representando as caracteristicas do cliente
    # todos eles foram criados usando o comando self, que indica
    # que eles pertencem a classe Cliente. Os atributos foram
    # declarados como privados. Para isso utilizamos 2 undescores
    """
    A classe Cliente gera novos clientes e pede alguns
    dados pessoais e é capaz de salvar o cliente
    """

    def __init__(self):
        self.__nome = ""
        self.__idade = 0
        self.__genero = ""
        self.__email = ""

    # O método dados é utilizado para realizar a passagem dos dados
    # do cliente para dentro da clase Cliente.
    def dados(self, nome="", idade=0, genero="", email=""):
        """
        O método dados pede algumas informações do cliente para que ele
        seja salvo no sistema
        """
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero
        self.__email = email

    # O método gravar exibe uma mensagem com o nome do cliente
    # dizendo que foi salvo com sucesso
    def gravar(self):
        """
        O método gravar exibe uma mensagem com o nome do cliente e
        gravação realizada com sucesso.
        """
        print("O cliente {} foi gravado com sucesso".format(self.__nome))
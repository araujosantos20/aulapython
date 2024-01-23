from class_conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self):
        self.__limite = 0.0
    
    def abrirConta(self, nb=0, na=0, nc="", titular="" ,saldo=0.0, limite=0.0):
        self._nbanco = nb
        self._nagencia = na
        self._nconta = nc
        self._titular = titular
        self._saldo = saldo
        self.__limite = limite
        print("A conta {} do Sr(a). {} foi aberta".format(self._nconta, self._titular))

    def sacar(self, valor):

        if (valor > self._saldo + self.__limite):
            print("Saldo insuficiente!")
        elif (valor <= self._saldo):
            self._saldo -= valor
            print("Você realizou um saque de {}, o seu saldo atual é {}".format(str(valor), str(self._saldo)))
        else:
            sobra = valor - self._saldo
            self.__limite -= sobra
            self._saldo = 0
            print("O valor retirado é R${} \nO saldo atual é: R${} \nO seu limite atual é: R${}".format(str(valor), str(self._saldo), str(self.__limite)))
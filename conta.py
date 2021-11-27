class Conta:
    # Construtor da classe
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        # Define os atributos privados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    # Definindo Método Privado
    def __pode_sacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # ################### #
    # GETTERS AND SETTERS #
    # ################### #

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # Cria método estático para definir código do banco
    # São métodos da classe. Não precisam de objetos para serem chamados
    @staticmethod
    def codigo_banco():
        return "001"

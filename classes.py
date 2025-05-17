from abc import ABC, abstractmethod


class Usuario:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id

    def __init__(self, nome, email, saldo):
        self.id = self.incremento_id()
        self.nome = nome
        self.email = email
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor


class Categoria:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id
    
    def __init__(self, nome, limite):
        self.id = self.incremento_id()
        self.nome = nome
        self.limite = limite
        self.__saldo = 0
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor      


class Transacao(ABC):   
    @abstractmethod
    def transacao(self):
        pass


class Pagamento(Transacao):
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id
    
    def __init__(self, nome, valor, data, forma_pagamento, categoria_id, conta_id):
        self.id = self.incremento_id()
        self.nome = nome
        self.valor = valor
        self.data = data
        self.forma_pagamento = forma_pagamento
        self.categoria_id = categoria_id
        self.conta_id = conta_id

    def transacao(self):
        pass


class Proventos(Transacao):
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id
    
    def __init__(self, nome, valor, data, conta_id):
        self.id = self.incremento_id()
        self.nome = nome
        self.valor = valor
        self.data = data
        self.conta_id = conta_id

    def transacao(self):
        pass


class Metas:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id
    
    def __init__(self, nome, valor, prazo):
        self.id = self.incremento_id()
        self.nome = nome
        self.valor = valor
        self. prazo = prazo
        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
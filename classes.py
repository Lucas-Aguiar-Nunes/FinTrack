from abc import ABC, abstractmethod


class Usuario:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id

    def __init__(self, id, nome, email, senha, idade):
        self.id = self.incremento_id()
        self.nome = nome
        self.email = email
        self.senha = senha #privado
        self.set_idade(idade)

    def set_idade(self, idade):
        while idade < 0:
            print("Idade Invalida!")
            idade = int("Idade tem que ser maior que 16: ")
        self.idade = idade


class Categoria:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id
    
    def __init__(self, nome, limite, saldo):
        pass


class Transacao(ABC):   
    @abstractmethod
    def transacao(self):
        pass


class Pagamento:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id


class Proventos:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id
    
    def __init__(self, id, descricao, valor, data, categoria_id, conta_id):
        self.id = self.incremento_id()


class Metas:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id += 1
        return cls.contador_id
    
    def __init__(self, id, nome, valor, saldo, prazo):
        self.id = self.incremento_id()
        self.nome = nome
        self.valor = valor
        self. prazo = prazo
        self.saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
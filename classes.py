from abc import ABC, abstractmethod


class Usuario:
    def __init__(self, id, nome, email, senha, idade):
        self.id = id
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
    pass

class Transacao(ABC):
    @abstractmethod
    def transacao(self):
        pass

class Pagamento:
    pass

class Lancamento:
    def __init__(self, id, descricao, valor, data, categoria_id, conta_id):
        self.id = id

class Metas:
    def __init__(self, id, nome, valor, saldo, prazo):
        self.id = id
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

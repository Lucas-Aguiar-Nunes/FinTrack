from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    moeda = 'R$'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    _saldo = Column("saldo", Float, default=0.0)

    pagamentos = relationship('Pagamento', back_populates='usuario')
    proventos = relationship('Provento', back_populates='usuario')
    metas = relationship('Meta', back_populates='usuario')

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @classmethod
    def alterar_moeda(cls, moeda):
        cls.moeda = moeda


class Categoria(Base):
    __tablename__ = 'categorias'

    moeda = 'R$'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    limite = Column(Float, nullable=False)
    _saldo = Column("saldo", Float, default=0.0)

    pagamentos = relationship('Pagamento', back_populates='categoria')

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @classmethod
    def alterar_moeda(cls, moeda):
        cls.moeda = moeda


class Transacao(Base):
    __abstract__ = True

    moeda = 'R$'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)

    def transacao(self):
        raise NotImplementedError("Subclasse precisa implementar o método transacao()")
    
    @classmethod
    def alterar_moeda(cls, moeda):
        cls.moeda = moeda


class Pagamento(Transacao):
    __tablename__ = 'pagamentos'

    forma_pagamento = Column(String, nullable=False)
    conta_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)  

    usuario = relationship('Usuario', back_populates='pagamentos')
    categoria = relationship('Categoria', back_populates='pagamentos')

    def transacao(self):
        if self.valor < 0: #type:ignore
            raise ValueError("Valor deve ser positivo.")
        if self.usuario is None or self.categoria is None:
            raise ValueError("Usuário ou categoria não vinculados corretamente.")
        if self.valor > self.usuario.saldo:
            raise ValueError("Valor deve ser menor que o saldo disponível.")
        self.usuario.saldo -= self.valor
        self.categoria.saldo += self.valor


class Provento(Transacao):
    __tablename__ = 'proventos'

    fonte = Column(String, nullable=False)
    conta_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='proventos')

    def transacao(self):
        if self.valor < 0: #type:ignore
            raise ValueError("Valor deve ser positivo.")
        if self.usuario is None:
            raise ValueError("Usuário não vinculado corretamente.")
        self.usuario.saldo += self.valor


class Meta(Base):
    __tablename__ = 'metas'

    moeda = 'R$'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    prazo = Column(Date, nullable=False)
    _saldo = Column("saldo", Float, default=0.0)
    conta_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='metas')

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @classmethod
    def alterar_moeda(cls, moeda):
        cls.moeda = moeda


engine = create_engine('sqlite:///controlefinanceiro.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
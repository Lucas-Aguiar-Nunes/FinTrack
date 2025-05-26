from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import date


engine = create_engine('sqlite:///controlefinanceiro.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    saldo = Column(Float, default=0.0)

    pagamentos = relationship('Pagamento', back_populates='usuario')
    proventos = relationship('Proventos', back_populates='usuario')


class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    limite = Column(Float, nullable=False)
    saldo = Column(Float, default=0.0)

    pagamentos = relationship('Pagamento', back_populates='categoria')


class Transacao(Base):
    __abstract__ = True 

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(Date, nullable=False)


class Pagamento(Transacao):
    __tablename__ = 'pagamentos'

    forma_pagamento = Column(String, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    conta_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    categoria = relationship('Categoria', back_populates='pagamentos')
    usuario = relationship('Usuario', back_populates='pagamentos')


class Proventos(Transacao):
    __tablename__ = 'proventos'

    conta_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship('Usuario', back_populates='proventos')


class Metas(Base):
    __tablename__ = 'metas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    prazo = Column(Date, nullable=False)
    saldo = Column(Float, default=0.0)


Base.metadata.create_all(engine)

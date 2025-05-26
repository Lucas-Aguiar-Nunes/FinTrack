from tabelas import *
from datetime import date

def adicionar_usuario(nome, email, saldo_inicial):
    usuario = Usuario(
        nome=nome, 
        email=email
    )
    usuario.saldo = saldo_inicial
    session.add(usuario)
    session.commit()
    return usuario

def adicionar_categoria(nome, limite, saldo_inicial=0.0):
    categoria = Categoria(
        nome=nome, 
        limite=limite
    )
    categoria.saldo = saldo_inicial
    session.add(categoria)
    session.commit()
    return categoria

def adicionar_pagamento(nome, valor, data, forma_pagamento, usuario_id, categoria_id):
    pagamento = Pagamento(
        nome=nome,
        valor=valor,
        data=data,
        forma_pagamento=forma_pagamento,
        conta_id=usuario_id,
        categoria_id=categoria_id
    )
    session.add(pagamento)
    session.commit()
    pagamento = session.query(Pagamento).get(pagamento.id)
    if pagamento is not None:
        pagamento.transacao()
    session.commit()
    return pagamento

def adicionar_provento(nome, valor, data, fonte, usuario_id):
    provento = Provento(
        nome=nome,
        valor=valor,
        data=data,
        fonte=fonte,
        conta_id=usuario_id,
    )
    session.add(provento)
    session.commit()
    provento = session.query(Provento).get(provento.id)
    if provento is not None:
        provento.transacao()
    session.commit()
    return provento

def adicionar_meta(nome, valor, prazo, usuario_id, saldo_inicial=0.0):
    meta = Meta(
        nome=nome,
        valor=valor,
        prazo = prazo,
        conta_id=usuario_id
    )
    meta.saldo = saldo_inicial
    session.add(meta)
    session.commit()
    return meta

def listar_usuarios():
    return session.query(Usuario).all()

def listar_categorias():
    return session.query(Categoria).all()

def listar_pagamentos():
    return session.query(Pagamento).all()

def listar_proventos():
    return session.query(Provento).all()

def listar_metas():
    return session.query(Meta).all()
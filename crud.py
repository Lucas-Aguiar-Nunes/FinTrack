from tabelas import *
from erros import *
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

def atualizar_usuario(usuario):
    print(f"{usuario.id} - {usuario.nome}\t| Email: {usuario.email}\t| Saldo: {usuario.moeda}{usuario.saldo}")
    try:
        nome = input("Nome do usuário: ")
        email = input("Email: ")
        if nome == "" or email == "":
            raise Campo_Vazio
        if "@" not in email:
            raise Email_Invalido
        saldo = float(input("Saldo inicial: "))
        if saldo < 0:
            raise Valor_Incorreto
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except Email_Invalido:
        print("Email Invalido. Tente Novamente.")
    except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
        print("Valor Deve ser Maior que 0. Tente Novamente.")
    else:
        usuario.nome = nome.upper()
        usuario.email = email.upper()
        usuario.saldo = saldo
        session.commit()
        print("Atualizado com Sucesso.")
    finally:
        sair = input("Pressione Qualquer Tecla Para Voltar...")

def adicionar_categoria(nome, limite, saldo_inicial=0.0):
    categoria = Categoria(
        nome=nome, 
        limite=limite
    )
    categoria.saldo = saldo_inicial
    session.add(categoria)
    session.commit()
    return categoria

def atualizar_categoria(categoria):
    print(f"{categoria.id} - {categoria.nome}\t| Limite: {categoria.moeda}{categoria.limite}\t| Saldo: {categoria.moeda}{categoria.saldo}")
    try:
        nome = input("Nome da categoria: ")
        if nome == "":
            raise Campo_Vazio
        limite = float(input("Limite: "))
        if limite <= 0:
            raise Valor_Incorreto
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
            print("Valor Deve ser Maior que 0. Tente Novamente.")
    else:
        categoria.nome = nome.upper()
        categoria.limite = limite
        session.commit()
        print("Atualizado com Sucesso.")
    finally:
        sair = input("Pressione Qualquer Tecla Para Voltar...")

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

def atualizar_pagamento(pagamento):
        print(f"{pagamento.id} - {pagamento.nome}\t| Conta: {pagamento.conta_id}\t| Categoria: {pagamento.categoria_id}\t| Valor: {pagamento.moeda}{pagamento.valor}\t| Forma: {pagamento.forma_pagamento}")
    try:
        nome = input("Nome do usuário: ")
        email = input("Email: ")
        if nome == "" or email == "":
            raise Campo_Vazio
        if "@" not in email:
            raise Email_Invalido
        saldo = float(input("Saldo inicial: "))
        if saldo < 0:
            raise Valor_Incorreto
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except Email_Invalido:
        print("Email Invalido. Tente Novamente.")
    except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
        print("Valor Deve ser Maior que 0. Tente Novamente.")
    else:
        usuario.nome = nome
        usuario.email = email
        usuario.saldo = saldo
        session.commit()
        print("Atualizado com Sucesso.")
    finally:
        sair = input("Pressione Qualquer Tecla Para Voltar...")

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

def atualizar_provento(provento):
        print(f"{provento.id} - {provento.nome}\t| Conta: {provento.conta_id}\t| Fonte: {provento.fonte}\t| Valor: {provento.moeda}{provento.valor}")
    try:
        nome = input("Nome do usuário: ")
        email = input("Email: ")
        if nome == "" or email == "":
            raise Campo_Vazio
        if "@" not in email:
            raise Email_Invalido
        saldo = float(input("Saldo inicial: "))
        if saldo < 0:
            raise Valor_Incorreto
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except Email_Invalido:
        print("Email Invalido. Tente Novamente.")
    except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
        print("Valor Deve ser Maior que 0. Tente Novamente.")
    else:
        usuario.nome = nome
        usuario.email = email
        usuario.saldo = saldo
        session.commit()
        print("Atualizado com Sucesso.")
    finally:
        sair = input("Pressione Qualquer Tecla Para Voltar...")

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

def atualizar_meta(meta):
        print(f"{meta.id} - {meta.nome}\t| Conta: {meta.conta_id}\t| Valor: {meta.moeda}{meta.valor}\t| Prazo: {meta.prazo}")
    try:
        nome = input("Nome do usuário: ")
        email = input("Email: ")
        if nome == "" or email == "":
            raise Campo_Vazio
        if "@" not in email:
            raise Email_Invalido
        saldo = float(input("Saldo inicial: "))
        if saldo < 0:
            raise Valor_Incorreto
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except Email_Invalido:
        print("Email Invalido. Tente Novamente.")
    except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
        print("Valor Deve ser Maior que 0. Tente Novamente.")
    else:
        usuario.nome = nome
        usuario.email = email
        usuario.saldo = saldo
        session.commit()
        print("Atualizado com Sucesso.")
    finally:
        sair = input("Pressione Qualquer Tecla Para Voltar...")



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
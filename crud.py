from tabelas import *
from erros import *
from datetime import datetime

def entrada_usuario(usuario=None):
    try:
        nome = input("Nome do usuário: ")
        email = input("Email: ")
        if nome == "" or email == "":
            raise Campo_Vazio
        if "@" not in email:
            raise Email_Invalido
        saldo = float(input("Saldo: "))
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
        if usuario:
            usuario.nome = nome.upper()
            usuario.email = email.upper()
            usuario.saldo = saldo
            mensagem = "Atualizado com Sucesso."
        else:
            usuario = Usuario(
                nome=nome.upper(), 
                email=email.upper()
            )
            usuario.saldo = saldo
            session.add(usuario)
            mensagem = "Cadastro com Sucesso."
        session.commit()
        print(mensagem)

def entrada_categoria(categoria=None):
    try:
        nome = input("Nome da categoria: ")
        if nome == "":
            raise Campo_Vazio
        limite = float(input("Limite: "))
        if limite <= 0:
            raise Valor_Incorreto
        saldo = float(input("Saldo: "))
        if saldo < 0:
            raise Valor_Incorreto
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except ValueError:
        print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
        print("Valor Deve ser Maior que 0. Tente Novamente.")
    else:
        if categoria:
            categoria.nome = nome.upper()
            categoria.limite = limite
            categoria.saldo = saldo
            mensagem = "Atualizado com Sucesso."
        else:
            categoria = Categoria(
                nome=nome, 
                limite=limite
            )
            categoria.saldo = saldo
            session.add(categoria)
            mensagem = "Cadastro com Sucesso."
        session.commit()
        print(mensagem)

def entrada_pagamento(pagamento=None):
    try:
        nome = input("Nome do pagamento: ")
        forma = input("Forma de pagamento: ")
        if nome == "" or forma == "":
            raise Campo_Vazio
        if not pagamento:
            valor = float(input("Valor: "))
            if valor <= 0:
                raise Valor_Incorreto
        data = input("Data (DD/MM/AAAA): ")
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            raise Data_Incorreta
        usuario_id = int(input("ID do usuário: "))
        usuario = session.query(Usuario).filter_by(id=usuario_id).first()
        if not usuario:
            raise ID_Incorreto
        categoria_id = int(input("ID da categoria: "))
        categoria = session.query(Categoria).filter_by(id=categoria_id).first()
        if not categoria:
            raise ID_Incorreto        
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
        print("Valor Deve ser Maior que 0. Tente Novamente.")
    except ID_Incorreto:
        print("ID não Encontrado. Tente Novamente")
    except Data_Incorreta:
        print("Data Invalida. Tente Novamente.")
    else:
        if pagamento:
            pagamento.nome = nome.upper()
            pagamento.forma_pagamento = forma.upper()
            pagamento.data = data
            pagamento.usuario_id = usuario
            pagamento.categoria_id = categoria
            mensagem = "Atualizado com Sucesso."
        else:
            pagamento = Pagamento(
                nome=nome.upper(),
                valor=valor,
                data=data,
                forma_pagamento=forma.upper(),
                conta_id=usuario_id,
                categoria_id=categoria_id
            )
            session.add(pagamento)
            session.commit()
            if pagamento.transacao():
                mensagem = "Cadastro com Sucesso."
            else:
                session.delete(pagamento)
                mensagem = ""
        session.commit()
        if mensagem != "":
            print(mensagem)

def entrada_provento(provento=None):
    try:
        nome = input("Nome do pagamento: ")
        fonte = input("Fonte do Provento: ")
        if nome == "" or fonte == "":
            raise Campo_Vazio
        if not provento:
            valor = float(input("Valor: "))
            if valor <= 0:
                raise Valor_Incorreto
        data = input("Data (DD/MM/AAAA): ")
        try:
            data = datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            raise Data_Incorreta
        usuario_id = int(input("ID do usuário: "))
        usuario = session.query(Usuario).filter_by(id=usuario_id).first()
        if not usuario:
            raise ID_Incorreto        
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
        print("Valor Deve ser Maior que 0. Tente Novamente.")
    except ID_Incorreto:
        print("ID não Encontrado. Tente Novamente")
    except Data_Incorreta:
        print("Data Invalida. Tente Novamente.")
    else:
        if provento:
            provento.nome = nome.upper()
            provento.fonte = fonte.upper()
            provento.data = data
            provento.usuario_id = usuario
            mensagem = "Atualizado com Sucesso."
        else:
            provento = Provento(
                nome=nome.upper(),
                valor=valor,
                data=data,
                fonte=fonte.upper(),
                conta_id=usuario_id,
            )
            session.add(provento)
            session.commit()
            if provento.transacao():
                mensagem = "Cadastro com Sucesso."
            else:
                session.delete(provento)
                mensagem = ""
        print(mensagem)
        session.commit()


def entrada_meta(meta=None):
    try:
        nome = input("Nome da Meta: ")
        if nome == "":
            raise Campo_Vazio
        valor = float(input("Valor Desejado: "))
        if valor <= 0:
            raise Valor_Incorreto
        saldo = float(input("Saldo: "))
        if saldo <= 0:
            raise Valor_Incorreto
        prazo = input("Data (DD/MM/AAAA): ")
        try:
            prazo = datetime.strptime(prazo, "%d/%m/%Y")
        except ValueError:
            raise Data_Incorreta
        usuario_id = int(input("ID do usuário: "))
        usuario = session.query(Usuario).filter_by(id=usuario_id).first()
        if not usuario:
            raise ID_Incorreto
    except Campo_Vazio:
        print("Campo Obrigatorio. Tente Novamente.")
    except ValueError:
        print("Valor Deve ser Numerico. Tente Novamente.")
    except Valor_Incorreto:
        print("Valor Deve ser Maior que 0. Tente Novamente.")
    except ID_Incorreto:
        print("ID não Encontrado. Tente Novamente")
    except Data_Incorreta:
        print("Data Invalida. Tente Novamente.")
    else:
        if meta:
            meta.nome = nome.upper()
            meta.valor = valor
            meta.prazo = prazo
            meta.conta_id = usuario_id
            meta.saldo = saldo
            mensagem = "Atualizado com Sucesso."
        else:
            meta = Meta(
                nome=nome,
                valor=valor,
                prazo = prazo,
                conta_id=usuario_id
            )
            meta.saldo = saldo
            session.add(meta)
            mensagem = "Cadastro com Sucesso."
        session.commit()
        print(mensagem)

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
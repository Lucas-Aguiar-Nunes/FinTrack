from crud import *
from erros import *
from datetime import datetime

def menu():
    while True:
        try:
            print("\t\tControle Financeiro")
            print("\t\tMenu")
            print("[1] - Inserir")
            print("[2] - Consultar")
            print("[3] - Atualizar")
            print("[4] - Deletar")
            print("[5] - Alterar Moeda")
            print("[0] - Sair ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                adicionar()
            elif escolha == "2":
                consultar()
            elif escolha == "3":
                atualizar()
            elif escolha == "4":
                deletar()
            elif escolha == "5":
                alterar_moeda()
            elif escolha == "0":
                break
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print(('Opção inválida. Tente novamente.'))
            sair = input("Pressione Qualquer Tecla Para Voltar...")
    print("Fechando Programa...")


def adicionar():
    while True:
        try:
            print("\t\tControle Financeiro")
            print("\t\tAdicionar no Banco de Dados")
            print("[1] - Usuario ")
            print("[2] - Meta ")
            print("[3] - Categoria ")
            print("[4] - Pagamento ")
            print("[5] - Provento ")
            print("[0] - Voltar ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                nome = input("Nome do usuário: ")
                email = input("Email: ")
                if nome == "" or email == "":
                    raise Campo_Vazio
                if "@" not in email:
                    raise Email_Invalido
                saldo = float(input("Saldo inicial: "))
                if saldo < 0:
                    raise Valor_Incorreto
                adicionar_usuario(nome.upper(), email.upper(), saldo)
                print("Cadastro com Sucesso.")
            elif escolha == "2":
                nome = input("Nome da Meta: ")
                if nome == "":
                    raise Campo_Vazio
                valor = float(input("Valor Desejado: "))
                if valor <= 0:
                    raise Valor_Incorreto
                saldo = float(input("Saldo inicial: "))
                if saldo <= 0:
                    raise Valor_Incorreto
                prazo = input("Prazo: ")
                usuario_id = int(input("ID do usuário: "))
                adicionar_meta(nome.upper(), valor, prazo, usuario_id, saldo)
                print("Cadastro com Sucesso.")
            elif escolha == "3":
                nome = input("Nome da categoria: ")
                if nome == "":
                    raise Campo_Vazio
                limite = float(input("Limite: "))
                if limite <= 0:
                    raise Valor_Incorreto
                adicionar_categoria(nome.upper(), limite)
                print("Cadastro com Sucesso.")
            elif escolha == "4":
                nome = input("Nome do pagamento: ")
                forma = input("Forma de pagamento: ")
                if nome == "" or forma == "":
                    raise Campo_Vazio
                valor = float(input("Valor: "))
                if valor <= 0:
                    raise Valor_Incorreto
                data = input("Data (DD/MM/AAAA): ")
                try:
                    data = datetime.strptime(data, "%d/%m/%Y")
                except ValueError:
                    raise Data_Incorreta
                usuario_id = int(input("ID do usuário: "))
                categoria_id = int(input("ID da categoria: "))
                adicionar_pagamento(nome.upper(), valor, data, forma.upper(), usuario_id, categoria_id)
                print("Cadastro com Sucesso.")
            elif escolha == "5":
                nome = input("Nome do provento: ")
                fonte = input("Fonte do Provento: ")
                if nome == "" or fonte == "":
                    raise Campo_Vazio
                valor = float(input("Valor: "))
                if valor <= 0:
                    raise Valor_Incorreto
                data = input("Data (DD/MM/AAAA): ")
                try:
                    data = datetime.strptime(data, "%d/%m/%Y")
                except ValueError:
                    raise Data_Incorreta
                usuario_id = int(input("ID do usuário: "))
                adicionar_provento(nome.upper(), valor, data, fonte.upper(), usuario_id)
                print("Cadastro com Sucesso.")
            elif escolha == "0":
                print("Voltando para Menu Principal")
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print(('Opção inválida. Tente Novamente.'))
        except Campo_Vazio:
            print("Campo Obrigatorio. Tente Novamente.")
        except Email_Invalido:
            print("Email Invalido. Tente Novamente.")
        except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
        except Valor_Incorreto:
            print("Valor Deve ser Maior que 0. Tente Novamente.")
        except Data_Incorreta:
            print("Data Invalida. Tente Novamente.")
        else:
            break
        finally:
            sair = input("Pressione Qualquer Tecla Para Voltar...")

def consultar():
    while True:
        try:
            print("\t\tControle Financeiro\n")
            print("\t\t Consultar no Banco de Dados\n")
            print("[1] - Usuario ")
            print("[2] - Meta ")
            print("[3] - Categoria ")
            print("[4] - Pagamento ")
            print("[5] - Provento ")
            print("[0] - Voltar ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                usuarios = listar_usuarios()
                for u in usuarios:
                    print(f"{u.id} - {u.nome}\t| Email: {u.email}\t| Saldo: {u.moeda}{u.saldo}")
            elif escolha == "2":
                metas = listar_metas()
                for m in metas:
                    print(f"{m.id} - {m.nome}\t| Conta: {m.conta_id}\t| Valor: {m.moeda}{m.valor}\t| Prazo: {m.prazo}")
            elif escolha == "3":
                categorias = listar_categorias()
                for c in categorias:
                    print(f"{c.id} - {c.nome}\t| Limite: {c.moeda}{c.limite}\t| Saldo: {c.moeda}{c.saldo}")
            elif escolha == "4":
                pagamentos = listar_pagamentos()
                for p in pagamentos:
                    print(f"{p.id} - {p.nome}\t| Conta: {p.conta_id}\t| Categoria: {p.categoria_id}\t| Valor: {p.moeda}{p.valor}\t| Forma: {p.forma_pagamento}")
            elif escolha == "5":
                proventos = listar_proventos()
                for p in proventos:
                    print(f"{p.id} - {p.nome}\t| Conta: {p.conta_id}\t| Fonte: {p.fonte}\t| Valor: {p.moeda}{p.valor}")
            elif escolha == "0":
                print("Voltando para Menu Principal.")
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print(('Opção inválida. Tente Novamente.'))
        else:
            break
        finally:
            sair = input("Pressione Qualquer Tecla Para Voltar...")

def atualizar():
    while True:
        try:
            print("\t\tControle Financeiro\n")
            print("\t\t Atualizar no Banco de Dados\n")
            print("[1] - Usuario ")
            print("[2] - Meta ")
            print("[3] - Categoria ")
            print("[4] - Pagamento ")
            print("[5] - Provento ")
            print("[0] - Voltar ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                id = int(input("Informe o ID do Usuário: "))
                usuario = session.query(Usuario).filter_by(id=id).first()
                if usuario:
                    atualizar_usuario(usuario)
                else:
                    raise ID_Incorreto
            elif escolha == "2":
                id = int(input("Informe o ID da Meta: "))
                meta = session.query(Meta).filter_by(id=id).first()
                if meta:
                    atualizar_meta(meta)
                else:
                    raise ID_Incorreto
            elif escolha == "3":
                id = int(input("Informe o ID da Categoria: "))
                categoria = session.query(Categoria).filter_by(id=id).first()
                if categoria:
                    atualizar_categoria(categoria)
                else:
                    raise ID_Incorreto
            elif escolha == "4":
                id = int(input("Informe o ID do Pagamento: "))
                pagamento = session.query(Pagamento).filter_by(id=id).first()
                if pagamento:
                    atualizar_pagamento(pagamento)
                else:
                    raise ID_Incorreto
            elif escolha == "5":
                id = int(input("Informe o ID do Provento: "))
                provento = session.query(Provento).filter_by(id=id).first()
                if provento:
                    atualizar_provento(provento)
                else:
                    raise ID_Incorreto
            elif escolha == "0":
                print("Voltando para Menu Principal.")
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print(('Opção inválida. Tente Novamente.'))
        except ID_Incorreto:
            print("ID não Encontrado. Tente Novamente")
        else:
            break
        finally:
            sair = input("Pressione Qualquer Tecla Para Voltar...")

def deletar():
    while True:
        try:
            print("\t\tControle Financeiro\n")
            print("\t\t Deletar no Banco de Dados\n")
            print("[1] - Usuario ")
            print("[2] - Meta ")
            print("[3] - Categoria ")
            print("[4] - Pagamento ")
            print("[5] - Provento ")
            print("[0] - Voltar ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                id = int(input("Informe o ID do Usuário: "))
                usuario = session.query(Usuario).filter_by(id=id).first()
                if usuario:
                    session.delete(usuario)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "2":
                id = int(input("Informe o ID da Meta: "))
                meta = session.query(Meta).filter_by(id=id).first()
                if meta:
                    session.delete(meta)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "3":
                id = int(input("Informe o ID da Categoria: "))
                categoria = session.query(Categoria).filter_by(id=id).first()
                if categoria:
                    session.delete(categoria)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "4":
                id = int(input("Informe o ID do Pagamento: "))
                pagamento = session.query(Pagamento).filter_by(id=id).first()
                if pagamento:
                    session.delete(pagamento)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "5":
                id = int(input("Informe o ID do Provento: "))
                provento = session.query(Provento).filter_by(id=id).first()
                if provento:
                    session.delete(provento)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "0":
                print("Voltando para Menu Principal.")
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print(('Opção inválida. Tente Novamente.'))
        except ID_Incorreto:
            print("ID não Encontrado. Tente Novamente")
        except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
        else:
            break
        finally:
            sair = input("Pressione Qualquer Tecla Para Voltar...")

def alterar_moeda():
    try:
        escolha = int(input("Digite [1] para Real (R$)\nDigite [2] para Dólar (U$)\n"))
        if escolha == 1:
            moeda = "RS"
        elif escolha == 2:
            moeda = 'U$'
        else:
            raise Escolha_Menu_Incorreta
    except Escolha_Menu_Incorreta:
        print("Entrada Invalida!")
    else:
        Usuario.alterar_moeda(moeda)
        Categoria.alterar_moeda(moeda)
        Pagamento.alterar_moeda(moeda)
        Provento.alterar_moeda(moeda)
        Meta.alterar_moeda(moeda)
    finally:
        sair = input("Pressione Qualquer Tecla Para Voltar...")   


if __name__ == "__main__":
    menu()
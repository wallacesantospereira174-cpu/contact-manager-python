memoria = {}

def menu():
    
    print(f"||{41*"="}||")
    print("|| =*= Sistema de Contatos do Wallace! =*= ||")
    print(f"||{41*"="}||")
    print("||     1 - Adicionar um Contato            ||")
    print("||     2 - Buscar um Contato               ||")
    print("||     3 - Listar todos os Contatos        ||")
    print("||     4 - Excluir contato                 ||")
    print("||     5 - Modificar número de usuario     ||")
    print("||     6 - Alterar e-mail                  ||")
    print("||     7 - Alterar nome                    ||")
    print("||     0 - Sair                            ||")
    print(f"||{41*"="}||")
    print("||         🤖🤖🤖🤖🤖🤖🤖🤖                ||")
    print(f"||{41*"="}||")
    

def adicionar_contato():
    nome = input("Nome:")     #confere
    chave_contato = (nome,)

    while True:
         try:
              
           numero = int(input("Numero de celular:"))
           break
         except ValueError:
              print("Erro de digitação")
              
    imail = input("E-mail:")
    if chave_contato in memoria:
        print(f'Contato {nome} já está salvo na sua lista de contatos!')
    else:
        memoria[chave_contato] = {
            "Numero":numero,
            "E-mail": imail,
        }
        print(f"\n Contato {nome} salvo com sucesso! ")

def  buscar_um_contato():
     buscar_contato = input("Nome do contato:")
     contato = (buscar_contato,)
     if contato in memoria:                           #confere
             informacoes = memoria[contato]

             print(f'Nome: {contato[0]}')
             print(f'Numero:{ informacoes["Numero"]}')
             print(f'E-mail:{ informacoes["E-mail"]}')

     else:
         print("Contato não salvo!")

def listar_todos_Contatos():   #confere
     for nome, informacoes in memoria.items():
             print(f'Nome: {nome[0]}')
             print(f'Numero:{ informacoes["Numero"]}')
             print(f'E-mail:{ informacoes["E-mail"]}')

def excluir_contato():
     buscar_contato = input("Nome do contato:")
     contato = (buscar_contato,)                         #confere
     if contato in memoria:
          memoria.pop(contato)
          print(f'Contato {buscar_contato} excluido!')
     else:
          print("Contato não encontrado.")

def pesquisar():
          while True:
               try:
                   opcao = int(input("Digite uma das opeção:"))
                   return opcao
               except ValueError:
                   print("Isso não é um número válido!")
                   
def alterar_numero():
        nome_contato = input("Nome de usuario:")
        contato = (nome_contato,)                       #confere
        if contato in memoria:
             
             while True:
                try:
                    numero = int(input("Novo número:"))
                    break
                except ValueError:
                     print("Erro tente novamente.")

             memoria[contato]["Numero"] = numero

             print("Numero atualizado com sucesso!")
        else:
             print("Contato não encontrado.")


def alterar_e_mail():
     nome = input("Nome de contato:")
     nome_contato = (nome,)
     if nome_contato in memoria:
          novo_e_mail = input("Novo E-mail:")
          while True:
              confirmar_alteracao = input("Confirmar alteração: S/N?").strip().lower()
              if confirmar_alteracao == "s":
                  memoria[nome_contato]["E-mail"] = novo_e_mail
                  print(f'E-mail alterado com sucesso!')
                  break
              elif confirmar_alteracao == "n":
                   print("E-mail não modificado!")
                   break
              else:
                   print("Digite apenas S ou N.")

     else:
          print("Contato não encontrado.") 
     
def alterar_nome():
     nome = input("Nome de usuario:")
     nome_usuario = (nome,)
     if nome_usuario in memoria:
          print(f'Nome atual{nome_usuario[0]}')
          informacoes = memoria[nome_usuario]

          novo_nome = input("Novo nome de usuario:")

          nova_chave = (novo_nome,)

          memoria[nova_chave] = informacoes

          memoria.pop(nome_usuario)

          print("Nome alterado com sucesso!")

     else:
          print("Contato não encontrado!") 


while True:
    menu()
    opcao = pesquisar()

    if opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        buscar_um_contato()

    elif opcao == 3:
         listar_todos_Contatos()

    elif opcao == 4:
         excluir_contato()

    elif opcao == 5:
          alterar_numero()

    elif opcao == 6:
         alterar_e_mail()

    elif opcao == 7:
         alterar_nome()

    elif opcao == 0:
         print("Sistema encerrado...")
         break

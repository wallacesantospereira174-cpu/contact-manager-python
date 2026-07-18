memoria = {}

def menu():
    
    print("||=========================================||")
    print("|| =*= Sistema de Contatos do Wallace! =*= ||")
    print("||=========================================||")
    print("||     1 - Adicionar um Contato            ||")
    print("||     2 - Buscar um Contato               ||")
    print("||     3 - Listar todos os Contatos        ||")
    print("||     4 - Excluir contato                 ||")
    print("||     5 - Modificar número de usuario     ||")
    print("||     0 - Sair                            ||")
    print("||=========================================||")
    print("||         🤖🤖🤖🤖🤖🤖🤖🤖                ||")
    print("||=========================================||")
    

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

def Listar_todos_Contatos():   #confere
     for nome, informacoes in memoria.items():
             print(f'Nome: {nome[0]}')
             print(f'Numero:{ informacoes["Numero"]}')
             print(f'E-mail:{ informacoes["E-mail"]}')

def Excluir_contato():
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



while True:
    menu()
    opcao = pesquisar()

    if opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        buscar_um_contato()

    elif opcao == 3:
         Listar_todos_Contatos()
    elif opcao == 4:
         Excluir_contato()
    elif opcao == 5:
          alterar_numero()
         
    elif opcao == 0:
         print("Sistema encerrado...")
         break

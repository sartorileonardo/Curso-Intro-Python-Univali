'''Faça um programa de cadastro de cliente, onde Cliente tem (codigo, nome, cpf, telefone, email, endereço).

O programa deve ter um menu com as opções(1- Cadastro, 2- Listar clientes, 3- Alterar cadastro, 4- Remover cliente).

O programa somente deve validar as entradas de dados CPF e Telefone, além de não permitir cadastro de nenhum campo vazio.

Caso o usuário tente inserir um valor vazio ou inválido, o sistema deve mostrar uma mensagem de erro e orientação ao usuário.

Para cada novo cadastro, alteração ou remoção de cliente, o programa deve exibir a lista de clientes disponíveis.

Após o cliente cadastrar ou alterar um cliente, o sistema deve exibir uma mensagem como: “Cliente cadastrado com sucesso!” ou “Cliente alterado com sucesso”.

O programa deve suportar ao menos 3 clientes.

Após cadastrar um cliente, o programa deve perguntar se o usuário deseja cadastrar um novo cliente, caso usuário escolha uma opção de NÃO, o programa deve exibir o menu de opções.

Dica1: Cada cliente pode ser armazenado em um Array, ex: cliente[codigo, nome, cpf, telefone, email, endereço].
'''
#!usr/bin/python

#Autor: Leonardo Sartori
#Curso: Introdução ao Desenvolvimento em Python

#Vetor que armazenará cliente
cli = []

print("------------- Menu do Sistema de Controle de Clientes ------------\n");
opc = int(0)

############## INICIO DAS FUNÇÕES ###############

#Função para add cliente
def add():
    cod = input("Digite o código do cliente:")
    name = input("Digite o nome do cliente:")
    cpf = input("Digite o cpf do cliente:")
    phone = input("Digite o telefone do cliente:")
    email = input("Digite o email do cliente:")
    address = input("Digite o endereço do cliente:")

    #Add elementos ao vetor
    cli.append(cod)
    cli.append(name)
    cli.append(cpf)
    cli.append(phone)
    cli.append(email)
    cli.append(address)

    print("\nO cliente " + cli[1] + " foi cadastrado com sucesso!\n")
    confirm = input("Deseja continuar no programa ? y/n\n")
    proceed(confirm)

#Função para verificar se o usuaário deseja continuar
def proceed(confirm):
    if confirm == "y":
        opc = 0
    else:
        opc = 5

#Função para listar cliente
def findAll():
    if len(cli) != 0:
            print("\nSegue dados do cliente cadastrado:\n")
            for i in range(len(cli)):
                print(cli[i])
                print("\n")
    else:
            print("\nNão há cliente(s) cadastrados no momento!\n")
            
#Função para alterar cliente
def change(codOfChange):
    if codOfChange == cli[0]:
            atrChange = input("Digite \n1-Trocar o nome \n2-Trocar o CPF \n3-Trocar o telefone \n4-Trocar o e-mail \n5-Trocar o enredeço\n")
            atrChange = int(atrChange)
            if atrChange == 1:
                cli[1] = input("Digite o novo nome:\n")
                print("O nome do cliente foi alterado com sucesso!")
            elif atrChange == 2:
                cli[2] = input("Digite o novo CPF:\n")
                print("O CPF do cliente foi alterado com sucesso!")
            elif atrChange == 3:
                cli[3] = input("Digite o novo felefone:\n")
                print("O telefone do cliente foi alterado com sucesso!")
            elif atrChange == 4:
                cli[4] = input("Digite o novo e-mail:\n")
                print("O e-mail do cliente foi alterado com sucesso!")
            elif atrChange == 5:
                cli[5] = input("Digite o novo endereço:\n")
                print("O endereço do cliente foi alterado com sucesso!")


############## FIM DAS FUNÇÕES ###############

while opc != 5:
    opc = input("Escolha apenas 1 das opções:\n1-Cadastro de novo cliente \n2-Listar clientes cadastrados \n3-Alterar um cliente cadastrado \n4-Remover um cliente cadastrado \n5-Sair do sistema\n")
    opc = int(opc)
    
    if opc == 1:
        add()

    elif opc == 2:
        findAll()

    elif opc == 3:
        codOfChange = input("Digite o código do cliente a ser alterado:\n")
        change(codOfChange)
        findAll()
    
    elif opc == 4:
        print("\nO cliente " + cli[1] + " foi removido com sucesso!\n")
        del(cli)
            
    elif opc == 5:
        print("Você saiu do sistema...")

    else:
        print("\nOpção inválida!\n")



    


    


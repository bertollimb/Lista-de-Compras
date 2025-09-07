from time import sleep
import os

lista_compra = []

def inserir_lista():
    item = input('O que gostaria de inserir na sua lista: ')
    lista_compra.append(item)
    print('Item adicionado com sucesso!')
    input("\nPressione ENTER para continuar...")

def mostrar_lista():
    if not lista_compra:
        print('Nenhum item encontrado!')
    else:
        print(f"{'ITENS':-^40}")
        for i, p in enumerate(lista_compra, 1):
            print(f"{i}. Item: {p}")
    input("\nPressione ENTER para continuar...")

def apagar_item():
    if not lista_compra:
        print('Nenhum item para excluir!')
        input("\nPressione ENTER para continuar...")
        return
    
    print(f"{'ITENS':-^40}")
    for i, p in enumerate(lista_compra, 1):
        print(f'{i}. Item: {p}')

    excluir_item = input('\nDigite o NÚMERO ou o NOME do item que deseja excluir: ').strip()

    # Tenta excluir pelo número
    if excluir_item.isdigit():
        indice = int(excluir_item) - 1
        if 0 <= indice < len(lista_compra):
            removido = lista_compra.pop(indice)
            print(f"Item '{removido}' removido com sucesso!")
        else:
            print("Número inválido!")
    
    # Tenta excluir pelo nome
    else:
        if excluir_item in lista_compra:
            lista_compra.remove(excluir_item)
            print(f"Item '{excluir_item}' removido com sucesso!")
        else:
            print("Item não encontrado!")

    input("\nPressione ENTER para continuar...")


def menu():
    print("""[ 1 ] ADICIONAR COMPRA
[ 2 ] MOSTRAR LISTA
[ 3 ] EXCLUIR ITEM
[ 4 ] SAIR""")

opcao = 0
while opcao != 4:
    os.system('cls')  # limpa a tela a cada volta
    menu()
    try:
        opcao = int(input('Qual sua opção: '))
    except ValueError:
        print('Digite um número válido!')
        input("\nPressione ENTER para continuar...")
        continue

    if opcao == 1:
        inserir_lista()
    elif opcao == 2:
        mostrar_lista()    
    elif opcao == 3:
        apagar_item()
    elif opcao == 4:
        print('Finalizando...')
        sleep(1.5)
    else:
        print('Opção inválida!')
        input("\nPressione ENTER para continuar...")

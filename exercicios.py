import os

pessoas = [{'nome' : 'IVAN' , 'idade' : 26, 'cidade': 'TUBARAO'}]

def adicionar_pessoas():
    nome = input('Nome: ')
    idade = input('Idade:')
    cidade = input('Cidade: ')
    nova_pessoa = {'nome' : nome , 'idade' : idade , 'cidade' : cidade}
    pessoas.append(nova_pessoa)
    voltar_ao_menu()

    



def listar_pessoas():
    print(f'{'Nome'.ljust(15)} | {'Idade'.ljust(5)} | cidade     ')

    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        
        print(f'- {nome.ljust(13)} | {idade}    | {cidade}')
    voltar_ao_menu()

def atualizar_dados():
    nome = input('Digite o nome para atualizar os dados: ').upper()
    for pessoa in pessoas:
        
        if nome == pessoa['nome']:
           opcao = int(input('1 - Alterar idade \n 2 - Alterar cidade '))
           if opcao == 1:
               nova_idade = input('nova idade: ').upper()
               pessoa['idade'] = nova_idade
               print(f'Idade alterada para {pessoa['idade']}')
           else: 
               nova_cidade = input('nova cidade: ').upper()
               pessoa['cidade'] = nova_cidade
               print(f'Idade alterada para {pessoa['cidade']}')
    voltar_ao_menu()
            
        
        

def opçoes():
    opcao = int(input(' 1- Adicionar Pessoa. \n 2- Listar Pessoas \n 3- Atualizar Dados' ))

    match opcao:
        case 1:
           
            adicionar_pessoas()
            
            
        case 2:
            
            listar_pessoas()

        case 3:
            atualizar_dados()

        case _ :
            print('erro')

def voltar_ao_menu():
    input('Digite qualquer tecla para voltar ao menu.')
    os.system('cls')
    main()



def main():
    os.system('cls')
    opçoes()






if __name__ == '__main__':
    main()

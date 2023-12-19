import os


restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False} ,
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def nome_app():
    print("""░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    
def opcoes():
    print('1. Cadastrarr Restaurante.')
    print('2. Listar Restaurantes.')
    print('3. Ativar Restaurantes.')
    print('4. Sair.')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def cadastrar_novo_restaurante():
    
    exibir_subtitulo('Cadastrar Novos Restaurantes')
    nome_restaurante = input('Nome do Novo Restaurante:').title()
    categoria = input(f'Digite a Categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria, 'ativo' : False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso')
    voltar_ao_menu()
2
def listar_restaurantes():
    
    exibir_subtitulo('Lista de Restaurantes Cadastros')
    for restaurante in restaurantes:
      
        print(f' - {restaurante['nome']} | {restaurante['categoria']} | {restaurante['ativo']} |')
 
    voltar_ao_menu()

def ativar_restaurante():
    exibir_subtitulo('Ativar Restaurantes')
    
    nome_restaurante = input('Digite o Nome do Restaurante: ')
    print(nome_restaurante)
    restaurante_encontrado = False

    for restaurante_ativo in restaurantes:
        if nome_restaurante == restaurante_ativo['nome']:
            restaurante_encontrado = True
            restaurante_ativo['ativo'] = not restaurante_ativo
            mensagem = 'restaurante ativado' if restaurante_ativo['ativo'] else 'restarante inativo'
            print(mensagem)
    if not restaurante_encontrado:
        print('restaurante nao cadastrado')
    



        
            
        

    voltar_ao_menu()


def voltar_ao_menu():
    input('Digite uma tecla para voltar ao menu principal.')
    main()
        


def finalizar_app():
    os.system('cls')
    print("finalizar app.\n")      

def escolher_opçoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))    
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()

            case 2:
                listar_restaurantes()

            case 3:
                ativar_restaurante()

            case 4:
                
                finalizar_app()   

            case _:
                opcao_invalida()     
    except:
        opcao_invalida()

def opcao_invalida():
    voltar_ao_menu()


            


def main():
    os.system('cls')
    nome_app()
    opcoes()
    escolher_opçoes()


if __name__ == "__main__":
    main()
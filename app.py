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
    '''ESSA FUNÇÃO MOSTRA AS OPÇOES NA TELA'''
    print('1. Cadastrarr Restaurante.')
    print('2. Listar Restaurantes.')
    print('3. Alterar Status do Restaurante.')
    print('4. Sair.')


def exibir_subtitulo(texto):
    '''ESSA FUNÇÃO IMPRIME O SUBTITULO EM TODAS AS OPÇOES/FUNÇOES'''
    linha = '*' * (len(texto))
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)


def cadastrar_novo_restaurante():
    '''ESSA FUNÇÃO CADASTRA UM NOVO RESTAURANTE
    Inputs:
    - nome do restaurante
    - categoria
    
    Outputs:
     - add um novo restaurante ao restaurantes[]'''
    
    exibir_subtitulo('Cadastrar Novos Restaurantes')
    nome_restaurante = input('Nome do Novo Restaurante:').title()
    categoria = input(f'Digite a Categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome' : nome_restaurante, 'categoria' : categoria, 'ativo' : False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso')
    voltar_ao_menu()


def listar_restaurantes():
    '''ESSA FUNÇÃO MOSTRA TODOS OS RESTAURANTES CADASTRADOS
    NOME,CATEGORIA,ATIVO/INATIVO'''
    
    exibir_subtitulo('Lista de Restaurantes Cadastros')

    print(f'{'Nome do Restaurante'.ljust(22)} | {'categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'Ativo' if restaurante['ativo'] else 'Inativo'
      
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}')
 
    voltar_ao_menu()


def ativar_restaurante():
    '''ESSA FUNÇÃO ATIVA/DESATIVA UM RESTAURANTE
    Inputs:
    - nome do restaurante
    Outputs:
    - altera o 'ativo' = true/false'''


    exibir_subtitulo('Ativar Restaurantes')
    
    nome_restaurante = input('Digite o Nome do Restaurante: ').title()
    
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('restaurante nao cadastrado')
    



        
            
        

    voltar_ao_menu()


def voltar_ao_menu():
    '''ESSA FUNÇÃO VOLTA PARA O MENU PRINCIPAL'''
    input('Digite uma tecla para voltar ao menu principal.')
    main()
        


def finalizar_app():
    '''ESSA FUNÇÃO SAI DO APP'''
    os.system('cls')
    print("finalizar app.\n")      

def escolher_opçoes():
    '''ESSA FUNÇÃO RECEBE A ESCOLHA DO USUARIO E
    CHAMA A FUNÇÃO CORRESPONDENTE
    Inputs:
    - recebe a escolha do usuario
    '''
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
    '''SE TIVER ALGUMA INPUT INVALIDO RETORNA AO MENU'''
    voltar_ao_menu()


            


def main():
    os.system('cls')
    nome_app()
    opcoes()
    escolher_opçoes()


if __name__ == "__main__":
    main()
from modelos.restaurante import Restaurante

import os


restaurante_praca = Restaurante('praça', 'Gourmet')
imirato = Restaurante('imigrato', 'italiana')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 5)
restaurante_praca.receber_avaliacao('Emy', 8)


def main():
    
    os.system('cls')
    Restaurante.listar_restaurante()



if __name__ == '__main__':
    main()
from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Será mostrado na tela'''
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    @classmethod
    def listar_restaurante(cls):
        ''' Exibe a lista formatada de todos os restaurante'''
        print(f'{'Nome'.ljust(20)} | {'Avaliações'.ljust(20)} | {'Categoria'.ljust(20)} Ativo')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo} ')

    @property
    def ativo(self):
        '''exibe um simbolo do estado do restaurante'''
        return '✅' if self._ativo else '❌'
    
    def alterar_estado(self):
        '''Altera o estado do restaurante'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''Recebe a nota do usuario
        Imputs: cliente , nota
        '''        
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao) 

    @property
    def media_avaliacoes(self):
        '''Calcula a a media da nota'''
        if not self._avaliacao:
            return 'Sem avaliaçoes'
        somas_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round( (somas_das_notas / quantidade_notas) ,1)
        return media
        
    
    
    



        

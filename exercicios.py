#1 Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, 
#  autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.


class Livro:
    def __init__(self, nome, autor,ano_publicado):
        self._livro = nome
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponvel = True

#2 Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, 
#  autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'Nome: {self._livro} Autor: {self._autor} Ano Publicado: {self._ano_publicado}'

#3 Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
#  Crie uma instância da classe, chame o método emprestar eimprima se o livro está disponível ou não.

    def emprestar(self):
        self._disponvel = False

#4 Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e 
#  retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade( ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis


livro1 = Livro('A lenda de ruff ghanor','jovem nerd', 2015)
livro2 = Livro('Percy Jacson', 'juliana', 2015)
livro3 = Livro("Aprendendo Python", "John Doe", 2022)
livro4 = Livro("Data Science Fundamentals", "Jane Smith", 2022)


     
print(livro1)
print(livro2)
print()
Livro.livros =  [livro1, livro2, livro3, livro4]


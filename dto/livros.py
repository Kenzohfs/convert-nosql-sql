class Livro:
    def __init__(self, isbn, titulo, edicao, preco):
        self.isbn = isbn
        self.titulo = titulo
        self.edicao = edicao
        self.preco = preco

    def to_string(self):
        return f'ISBN: {self.isbn}, Título: {self.titulo}, Edição: {self.edicao}'

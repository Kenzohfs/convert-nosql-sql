class AutorLivro:
    def __init__(self, id, idAutor, isbnLivro):
        self.id = id
        self.idAutor = idAutor
        self.isbnLivro = isbnLivro

    def to_string(self):
        return f'ID: {self.id}, ID Autor: {self.idAutor}, ISBN Livro: {self.isbnLivro}'

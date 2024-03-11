class Autor:
    def __init__(self, id, nome, sobrenome):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome

    def to_string(self):
        return f'ID: {self.id}, Nome: {self.nome}, Sobrenome: {self.sobrenome}'

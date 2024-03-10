class Autor:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def to_string(self):
        return f'Nome: {self.nome}, Sobrenome: {self.sobrenome}'

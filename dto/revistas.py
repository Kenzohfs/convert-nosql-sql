class Revista:
    def __init__(self, ano, mes, titulo):
        self.ano = ano
        self.mes = mes
        self.titulo = titulo

    def to_string(self):
        return f'Ano: {self.ano}, Mês: {self.mes}, Título: {self.titulo}'
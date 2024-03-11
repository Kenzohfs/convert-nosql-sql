import pandas as pd
import json
from dto.livros import Livro
from dto.autores import Autor
from dto.autorLivro import AutorLivro
from dto.revistas import Revista

file = open('dataset.json', encoding='utf-8')
data = json.load(file)

livros = []
autores = []
autorLivro = []

titulo = 'Título'
isbn = 'ISBN'
edicao = 'Edição'
preco = 'Preço'

autorNome = 'Nome'
autorSobrenome = 'Sobrenome'

for livro in data['Livros']:
    livroObject = Livro(None, None, None, None)

    if livro.get(edicao):
        livroObject.edicao = livro[edicao]

    if livro.get(preco):
        livroObject.preco = livro[preco]

    if livro.get(isbn):
        livroObject.isbn = livro[isbn]

    if livro.get(titulo):
        livroObject.titulo = livro[titulo]

    livros.append(livroObject)

    for autor in livro['Autores']:
        autorObject = Autor(None, None, None)

        if autor.get(autorNome):
            autorObject.nome = autor[autorNome]

        if autor.get(autorSobrenome):
            autorObject.sobrenome = autor[autorSobrenome]

        for autorAux in autores:
            if autorAux.nome == autorObject.nome and autorAux.sobrenome == autorObject.sobrenome:
                autorObject.id = autorAux.id

        if not autorObject.id:
            autorObject.id = len(autores) + 1
            autores.append(autorObject)

        relationship = AutorLivro(
            len(autorLivro) + 1, autorObject.id, livroObject.isbn)
        autorLivro.append(relationship)


for livro in livros:
    print(livro.to_string())

for autor in autores:
    print(autor.to_string())

for relationship in autorLivro:
    print(relationship.to_string())


livros_dict = [livro.__dict__ for livro in livros]
livrosDf = pd.DataFrame(livros_dict)

livrosDf.to_csv('output/livros.csv', index=False)

autores_dict = [autor.__dict__ for autor in autores]
autoresDf = pd.DataFrame(autores_dict)

autoresDf.to_csv('output/autores.csv', index=False)

autor_livro_dict = [autorLivro.__dict__ for autorLivro in autorLivro]
autorLivroDf = pd.DataFrame(autor_livro_dict)

autorLivroDf.to_csv('output/autoresLivros.csv', index=False)

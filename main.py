import pandas as pd
from dto.livros import Livro

livro1 = Livro('978-85-333-0223-4', 'Python Fluente', None)
print(livro1.to_string())

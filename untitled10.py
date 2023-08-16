import pandas as pd

serie = pd.Series([5, 7, 12, 2, 1, 6, 7, 0,-3, 22])
print(f'Valor mais alto: {serie.max()}')
print(f'Indice do maior valor: {serie.idxmax()}')
print(f'Indice do menor valor: {serie.idxmin()}')
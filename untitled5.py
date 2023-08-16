import pandas as pd

dicionario = {'Ano': 1950, 
    'Item': 'TV',
    'Preco': 250.60
}
serie = pd.Series(dicionario)
print(serie)
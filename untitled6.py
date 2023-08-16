import pandas as pd

dicionario = {'EUA': 0, 'Inglaterra': 1, 'Argentina': 3, 'Brasil': 5,}
dados = pd.Series(dicionario)
print(dados)

print(dados.values)
print(dados.index)
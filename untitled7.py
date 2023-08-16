import pandas as pd
dados = pd.Series([12,34,21,-9,0,7], index = ['a','b','c','d','e','f',])
print ('Dado no indice C: ', dados['c'])
print ('\nindice b e e:')
print (dados[['b', 'e']])
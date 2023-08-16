import pandas as pd

serie = pd.Series([10,20,30,40,50],index = ['Num 1','Num 2','Num 3','Num 4','Num 5'])
print('Item na posição 0:', serie[0])
print('Item de indice Num 3:', serie['Num 3'])
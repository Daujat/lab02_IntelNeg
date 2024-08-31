import pandas as pd

archivo=pd.read_csv('Ventas.csv')
data=pd.DataFrame(archivo)

print(data)
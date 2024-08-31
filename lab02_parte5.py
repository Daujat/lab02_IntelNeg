import pandas as pd
import numpy as np

data=pd.DataFrame(np.array([['Enero', 'Febrero', 'Marzo'],
                            [23000, 50000, 40000],
                            [33000, 10000, 90000],
                            [43000, 70000, 80000] ]))

print(data)

###############b

print('Numero de filas y columnas: ', data.shape)
print('Numeor de filas: ', len(data.index))
print('Numeor de columnas: ', len(data.count()))

###############c

ventas_numerico = data.iloc[1:, :].astype(float)  # Convertir los valores a tipo numérico

#media
media = ventas_numerico.mean(axis=1)
print("\nMedia de las ventas:", media)

#correlación
correlacion = ventas_numerico.corr()
print("\nCorrelación:", len(correlacion))

#valor más bajo
valor_min = ventas_numerico.min().min()
print("\nValor más bajo:", valor_min)

#valor más alto
valor_max = ventas_numerico.max().max()
print("Valor más alto:", valor_max)

#mediana
mediana = ventas_numerico.median(axis=1)
print("Mediana:", mediana)

#desviación estándar
desviacion_estandar = ventas_numerico.std(axis=1)
print("Desviación estándar:", desviacion_estandar)

#la primera columna del dataset
primera_columna = data.iloc[:, 0]
print("\nPrimera columna del dataset:")
print(primera_columna)

#las 2 primeras columnas
dos_primeras_columnas = data.iloc[:, :2]
print("\nLas 2 primeras columnas del dataset:")
print(dos_primeras_columnas)

#primera fila
primera_fila = data.iloc[0]
print("\nPrimera fila del dataset:")
print(primera_fila)

#última columna
ultima_columna = data.iloc[:, -1]
print("\nÚltima columna del dataset:")
print(ultima_columna)

#valores de la primera fila
valores_primera_fila = data.iloc[0].values
print("\nValores de la primera fila:", len(valores_primera_fila))
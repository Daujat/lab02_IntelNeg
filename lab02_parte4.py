import pandas as pd
ventas_recilado={'Meses':['Enero','Febrero','Marzo'],
        'Monto':[23000,50000,40000]}

ventas_recilado2={'Meses':['Enero','Febrero','Marzo'],
        'Monto':[80000,90000,10000]}

data1=pd.DataFrame(ventas_recilado)
data2=pd.DataFrame(ventas_recilado2)

print(data1)
print(data2)

################

datos=data1.add(data2)
print(datos)

################

# Agregar el arreglo 2 sobre el arreglo 1
data_combined = pd.concat([data1, data2], ignore_index=True)

# Imprimir los datos combinados
print(data_combined)
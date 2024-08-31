import pandas as pd

###################A

ventas={'Meses':['Enero','Febrero','Marzo'],
        'Monto':[23000,50000,40000]}
data1=pd.DataFrame(ventas)

print(data1)

###################B

data2=pd.DataFrame(ventas, columns=['Monto', 'Meses'])

print(data2)

###################C
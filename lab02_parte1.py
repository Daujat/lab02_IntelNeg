import pandas as pd
import numpy as np
from sympy.stats.sampling.sample_numpy import numpy


#################a

data=pd.Series(['Enero','Febrero','Marzo',
                'Abril','Mayo','Junio'],index=[1,2,3,4,5,6])

print(data)

##########################b

data2=pd.Series({'David':4, 'Analu':5, 'Jaiden':6})

print(data2)

##########################c

data3=pd.Series(np.random.randn(10),index=[1,2,3,4,5,6,7,8,9,10])

print(data3.head(5))
print(data3.tail(5))
print(data3.head(2))
print(data3.tail(2))
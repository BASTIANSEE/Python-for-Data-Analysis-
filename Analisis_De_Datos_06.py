import numpy as np
import pandas as pd

#Crear arreglo de una dimension con 5 elementos 

arr1= np.array([1,2,3,4,5,6,5,6,5,5,5,5,6])

#Suma

suma=np.sum(arr1)
print(suma)

#Producto 

Producto=np.prod(arr1)
print(Producto)

#Promedio

promedio=np.mean(arr1)
print(promedio)

#Mediana

mediana=np.median(arr1)
print(mediana)

#Moda 
# Encontrar valores únicos y sus recuentos
valores, recuentos = np.unique(arr1, return_counts=True)

indice_moda = np.argmax(recuentos)
moda = valores[indice_moda]
print(moda)
               
#Varianza

varianza=np.var(arr1)
print(varianza)

#Desviacion estandar

Desv=np.std(arr1)
print(Desv)

#Max

Maximo=np.max(arr1)
print(Maximo)

#Max

Minimo=np.min(arr1)
print(Minimo)

#Suma acumulativa

cumsum=np.cumsum(arr1)
print(cumsum)

#Operaciones elemento elemento

print(arr1+arr1)
print(arr1-arr1)
print(arr1*arr1)
print(arr1/arr1)

#PANDAS Y NUMPY

#Crear array numpy

data=np.array([[1,2,3],[4,5,6],[7,8,9]])

#Crear un dataframe a traves de un array 

df=pd.DataFrame(data,columns=["A","B","C"])
print(df)

#Crear dataframe pandas

data={
    "A":[1,4,7],
    "B":[2,5,8],
    "C":[3,6,9]}

df=pd.DataFrame(data)
print(df)

#Crear un array a traves de dataframe

arr=df.to_numpy()
print(arr)

#Otra forma 

print(df.values)

#Calcular el promedio de cada columna usando numpy

mean_colums=np.mean(df, axis=0)
print(mean_colums)

#Forma directa con pandas axis 0=colum 1=filas

print(df.mean(axis=0))
print(df.mean(axis=1))
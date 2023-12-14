#ANALISIS DE COMPONENTES PRINCIPALES
#Tecnica PCA

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

from sklearn.decomposition import PCA 

#CUANDO SE TIENE DATOS CON MUCHAS DIMENSIONES NO SE PUEDE GRAFICAR, ENTONCES PCA REDUCE LA DIMENSION

df=sns.load_dataset("iris")
print(df)

print(df.iloc[:,:-1]) #Selecciona todas las filas menos la ultima

pca_model=PCA(n_components=2) #Se reduce a dos componetes
df_pca=pca_model.fit_transform(df.iloc[:,:-1]) #Entrena al modelo PCA y regresa los valores transformados
print(df_pca)

plt.scatter(df_pca[:,0], df_pca[:,1],c=df["species"].astype("category").cat.codes)
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.show()

#En resumen, este código toma los datos originales, los reduce a dos dimensiones usando PCA 
# y luego muestra un gráfico de dispersión de estos datos reducidos. Los puntos se colorean 
# según la categoría presente en la columna "species", lo que ayuda a visualizar la agrupación 
# o distribución de las diferentes categorías en el nuevo espacio dimensional.
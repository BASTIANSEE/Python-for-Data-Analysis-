#TRANSFORMACIÓN DE VARIABLES

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

from sklearn.decomposition import PCA 

#CUANDO SE TIENE DATOS CON MUCHAS DIMENSIONES NO SE PUEDE GRAFICAR, TAMBIEN SE PUEDE APLICAR 
#TRANSFORMACIÓN DE VARIABLES

df=sns.load_dataset("iris")
print(df)

#CASO GENERAL 

sns.displot(data=df,x="sepal_length", hue="species",kde=True)
plt.show()

#NO SE PUEDEN VISUALIZAR LOS DATOS Y SEGMENTAR DE LA MEJOR MANERA
#LA SOLUCION ES SEPARAR LAS CLASES EN ESTE CASO POR LA SEPARACION LOGARITMICA

#transformacion logaritmica

df["sepal_length_log"]=np.log(df["sepal_length"])
sns.displot(data=df, x="sepal_length_log", hue="species", kde=True)
plt.show()

#LA FRECUENCIA CAMBIA Y LAS CUENTAS DE LOS GRUPOS DE DISTRIBUYEN DE MEJOR FORMA
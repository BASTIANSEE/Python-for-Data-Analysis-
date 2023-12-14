#Técnica de Escalado y Normalización de Datos
#CUANDO SE TRABAJA CON MILES DE TIPOS DE DATOS, NO TODOS LOS DATOS SON DEL MISMO TAMAÑO, HAY TAMAÑOS,
#DIMENSIONES, ECT. CUANDO SE QUIERE INTEGRAR NUEVOS DATOS SIEMPRE HAY UN LIMITE EN LOS QUE SE DEBE REENTRENAR
#EL MODELO PARA QUE PUEDA SER CAPAZ DE IDENTIFICAR EL DATO A TRAVES DE UNA DISTRIBUCIÓN.

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

from sklearn.preprocessing import StandardScaler,MinMaxScaler

#StandardScaler  estandariza los datos eliminando la media y escalando los datos de forma que su varianza sea
#=1  genera una distribucion normal y cuantas desviaciones estandar esta con respecto a su media


df=sns.load_dataset("iris")

std_scaler=StandardScaler()
df_std_scaler=std_scaler.fit_transform(df.iloc[:,:-1])
print(df_std_scaler)

#ESTANDARIZADO CON RESPECTO A SU MEDIA

# MinMaxScaler Se transforma las carracteristicas escalandolas a un rango dado por defecto de 0 a 1

mm_scaler=MinMaxScaler()
df_normalized=mm_scaler.fit_transform(df.iloc[:,:-1])
print(df_normalized)

#NORMALIZADO DE 0 A 1 

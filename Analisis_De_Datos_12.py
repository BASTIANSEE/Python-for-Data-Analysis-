#Caso practico

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(style="darkgrid")

df=sns.load_dataset("tips")
print(df)

#Grafico de barras propina promedio por sexo 

sns.barplot(data=df,x="sex", y="tip", errorbar=None)
plt.show()

## HOMBRES EN PROMEDIO PAGAN MÁS PROPINA

#Grafico propinas promedio por dia

sns.barplot(data=df,x="day", y="tip", errorbar=None)
plt.title("Propinas promedio por dias")
plt.show()

##LOS DOMINGOS SE OBTIENE MÁS PROPINAS

#Grafico de propinas promedio por tiempo

sns.barplot(data=df,x="time", y="tip", errorbar=None)
plt.title("Propinas promedio por tiempo")
plt.show()

##EN LA CENA SE OBTIENE MÁS PROPINAS 

#Grafico de propinas promedio por clientes fumadores

sns.barplot(data=df,x="smoker", y="tip", errorbar=None)
plt.title("Propinas promedio por fumador")
plt.show()

##NO AFECTA EN LA PROPINA SI EL CLIENTE ES FUMADOR O NO

#MULTIVARIADO

#Grafico de barras de propinas promedio (dia, sexo)

sns.barplot(data=df, x="day", y="tip", hue="sex", errorbar=None)
plt.title("Promedio de propinas por dia y sexo")
plt.show()

#Grafico de barras de propinas promedio (timepo, sexo)

sns.barplot(data=df, x="time", y="tip", hue="sex", errorbar=None)
plt.title("Promedio de propinas por tiempo y sexo")
plt.show()

#Grafico de barras de propinas promedio (fumador, sexo)

sns.barplot(data=df, x="smoker", y="tip", hue="sex", errorbar=None)
plt.title("Promedio de propinas por fumador y sexo")
plt.show()

#Grafico de barras de propinas promedio (tamaño de mesa, sexo)

sns.barplot(data=df, x="size", y="tip", hue="sex", errorbar=None)
plt.title("Promedio de propinas por tamaño de mesa y sexo")
plt.show()


#Grafico de relación entre el tamaño de mesa y las propinas

sns.scatterplot(data=df, x="size", y="tip")
plt.title("Promedio de propinas por tamaño de mesa")
plt.show()

#Calcular el porcentaje de propina y agg al dataframe

df["tip_percentage"]=(df["tip"]/df["total_bill"])*100
print(df)

#Grafico de barras de porcentaje promedio de proponas por sexo

sns.barplot(data=df, x="sex", y="tip_percentage", errorbar=None)
plt.title("porcentaje promedio de proponas por sexo")
plt.show()

##DE ALGUNA MANERA A PESAR DE QUE LOS HOMBRES DEJEN MÁS DINERO, LAS MUJERES DAN MÁS PORCENTAJE
##DE ACUERDO A SU CUENTA TOTAL CONSUMIDA 

#Grafico de barras de porcentaje promedio de proponas por dia

sns.barplot(data=df, x="day", y="tip_percentage", errorbar=None)
plt.title("porcentaje promedio de proponas por dia")
plt.show()

## EL PROMEDIO DE PROPINA SE MANTIENE INDEPENDIENTEMENTE DEL DIA 

#Grafico de barras de porcentaje promedio de proponas por tiempo

sns.barplot(data=df, x="time", y="tip_percentage", errorbar=None)
plt.title("porcentaje promedio de proponas por tiempo")
plt.show()

## EL PROMEDIO DE PROPINA SE MANTIENE INDEPENDIENTEMENTE DEL TIEMPO

#Grafico de barras de porcentaje promedio de propinas por fumadores

sns.barplot(data=df, x="smoker", y="tip_percentage", errorbar=None)
plt.title("porcentaje promedio de proponas por fumadores")
plt.show()

## EL PROMEDIO DE PROPINA SE MANTIENE INDEPENDIENTEMENTE SI LA PERSONA FUMA O NO 



#Analisis Bivariado y Multivariado

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(style="darkgrid")

df=sns.load_dataset("tips")
print(df)

#Saber con que estamos trabajando 

print(df.info())
print(df.describe())

#Por lo general responde ¿Si mi cuenta es más costosa mi propina sera mas grande? 

sns.scatterplot(data=df, x="total_bill", y="tip")
plt.show()

#Por lo general responde ¿Dependiendo de mi sexo dejare  propina? 

sns.barplot(data=df, x="sex", y="tip")
plt.show()

#Gasto más si soy hombre o mujer 

sns.boxplot(data=df, x="sex", y="total_bill")
plt.show()

#MULTIVARIADO

sns.pairplot(df,hue="sex")
plt.show()
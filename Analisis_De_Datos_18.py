import numpy as np
import seaborn as sns
import pandas as pn 
import matplotlib.pyplot as plt

#Técnica Z-Score PARA DETECTAR OUTLIERS 

df=sns.load_dataset("iris")
print(df)

#Calcular Z-Score

df["z_score_sepal_lenght"]=np.abs((df["sepal_length"]-df["sepal_length"].mean())/df["sepal_length"].std())
print(df)

#Identificar outliers

outliers=df[df["z_score_sepal_lenght"]>2]
print(outliers)

# Crear un nuevo DataFrame sin los outliers
df_no_outliers = df[df["z_score_sepal_lenght"] <= 2]

# Mostrar información del nuevo DataFrame sin outliers
print(df_no_outliers)

# Crear dos gráficos de dispersión, uno con outliers y otro sin ellos
plt.figure(figsize=(12, 6))

# Gráfico de dispersión con outliers
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", style="species")
plt.scatter(outliers["sepal_length"], outliers["sepal_width"], color='red', s=100, label='Outliers')
plt.title('Con Outliers')
plt.legend()

# Gráfico de dispersión sin outliers
plt.subplot(1, 2, 2)
sns.scatterplot(data=df_no_outliers, x="sepal_length", y="sepal_width", hue="species", style="species")
plt.title('Sin Outliers')

# Ajustes de diseño y visualización
plt.tight_layout()
plt.show()

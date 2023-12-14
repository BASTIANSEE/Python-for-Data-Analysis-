#Analisis Exploratorio y Analisis Univariado

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


# Contar la cantidad de cada categoría en las columnas 'sex', 'smoker', 'day' y 'time'
sex_counts = df['sex'].value_counts()
smoker_counts = df['smoker'].value_counts()
day_counts = df['day'].value_counts()
time_counts = df['time'].value_counts()

# Obtener los valores y etiquetas para los gráficos de pastel
sex_labels = sex_counts.index.tolist()
sex_sizes = sex_counts.values.tolist()

smoker_labels = smoker_counts.index.tolist()
smoker_sizes = smoker_counts.values.tolist()

day_labels = day_counts.index.tolist()
day_sizes = day_counts.values.tolist()

time_labels = time_counts.index.tolist()
time_sizes = time_counts.values.tolist()

# Crear una figura con subplots para los cuatro gráficos
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico de pastel para 'sex'
axs[0, 0].pie(sex_sizes, labels=sex_labels, autopct='%1.1f%%', colors=['#FF5733', '#33FFC7'])
axs[0, 0].set_title('Distribución por Género')

# Gráfico de pastel para 'smoker'
axs[0, 1].pie(smoker_sizes, labels=smoker_labels, autopct='%1.1f%%', colors=['#FFCC99', '#99FF99'])
axs[0, 1].set_title('Distribución de Fumadores')

# Gráfico de pastel para 'day'
axs[1, 0].pie(day_sizes, labels=day_labels, autopct='%1.1f%%', colors=['#FFD700', '#C71585', '#00CED1', '#7CFC00'])
axs[1, 0].set_title('Distribución por Día')

# Gráfico de pastel para 'time'
axs[1, 1].pie(time_sizes, labels=time_labels, autopct='%1.1f%%', colors=['#FFA07A', '#6495ED'])
axs[1, 1].set_title('Distribución por Tiempo')

# Ajustar diseño y mostrar gráficos
plt.tight_layout()
plt.show()

#Histograma

sns.histplot(data=df,x="total_bill")
plt.show()

#Diagrama de caja

sns.boxplot(data=df,x="total_bill")
plt.show()

#Histograma del precio

sns.kdeplot(data=df, x="total_bill")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Establecer colores personalizados
colors = ['#FF5733', '#33FFC7', '#336BFF']  # Puedes ajustar los colores según tu preferencia

# Crear una figura con tres subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Histograma
sns.histplot(data=df, x="total_bill", ax=axs[0], color=colors[0])
axs[0].set_title('Histograma')

# Diagrama de caja
sns.boxplot(data=df, x="total_bill", ax=axs[1], color=colors[1])
axs[1].set_title('Diagrama de Caja')

# Histograma con distribución de densidad
sns.kdeplot(data=df, x="total_bill", ax=axs[2], color=colors[2])
axs[2].set_title('Histograma con KDE')

# Ajustar diseño y mostrar gráficos
plt.tight_layout()
plt.show()



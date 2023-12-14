import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

#Cargar base de datos 

data= sns.load_dataset("iris")
print(data)

#Ver cuantos tipos de species hay 

print(data, set(data["species"]))

#Grafica de disperción 

sns.scatterplot(x="sepal_length", y="sepal_width", hue="species",data=data)
plt.xlabel("Long sepalo")
plt.ylabel("Anch sepalo")
plt.title("IRIS DATA BASE")
plt.show()

#Grafica de Ridgeplot

setosa=data[data["species"]=="setosa"]
versicolor=data[data["species"]=="versicolor"]
virginica=data[data["species"]=="virginica"]

#Configuracion de figura y ejes

fig, ax= plt.subplots(figsize=(8,6))
plt.xlabel ("longitud del petalo")

#Crear el ridge plot usando kdeplot

sns.kdeplot(data=setosa["petal_length"], label="setosa", ax=ax, fill=True)
sns.kdeplot(data=versicolor["petal_length"], label="versicolor", ax=ax, fill=True)
sns.kdeplot(data=virginica["petal_length"], label="virginica", ax=ax, fill=True)

#ajustamos la posicion de las leyendas

ax.legend(loc="upper right")

plt.title("Ridge Plot- Iris Data Base")
plt.show()

#Grafica personalizada 

sns.set_style("whitegrid")
palette=sns.color_palette("husl",3)

sns.scatterplot(x="sepal_length", y="sepal_width", hue="species",data=data, palette=palette)
plt.xlabel("Long sepalo")
plt.ylabel("Anch sepalo")
plt.title("IRIS DATA BASE")
plt.show()

#Graficos avanzados

#Generar datos aleatorios

edad_autos=np.random.randint(0,20, size=200)
precio_autos=30-edad_autos+np.random.normal(-3,3, size=200)
data=pd.DataFrame({
    "edad":edad_autos,
    "precio":precio_autos
})

print(data)

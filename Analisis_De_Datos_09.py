#GRAFICOS AVANZADOS

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

#Generar datos aleatorios

np.random.seed(42)
edad_autos=np.random.randint(0,20, size=200)
precio_autos=30-edad_autos+np.random.normal(-3,3, size=200)
data=pd.DataFrame({
    "edad":edad_autos,
    "precio":precio_autos
})

print(data)

#Creación del grafico 

fig,ax=plt.subplots(2,2,figsize=(12,10))

#Grafico de disperción

ax[0,0].scatter(data["edad"], data["precio"], alpha=0.5)
ax[0,0].set_xlabel("Edad automovil (años)")
ax[0,0].set_ylabel("Precio (en miles de dolares)")
ax[0,0].set_title("Edad vs Precio")

#Histograma de la edad

sns.histplot(data["edad"], ax=ax[0,1], kde=True,color="g")
ax[0,1].set_xlabel("Edad automovil (años)")
ax[0,1].set_ylabel("Frecuencia")
ax[0,1].set_title("Histograma de Edad Auto")

#Histograma del precio

sns.histplot(data["precio"], ax=ax[1,0], kde=True,color="b")
ax[1,0].set_xlabel("Precio (en miles de dolares)")
ax[1,0].set_ylabel("Frecuencia")
ax[1,0].set_title("Histograma de Precio Auto")

#Eliminar 4to subplot

ax[1,1].axis("off")

#Ajustar espacio altura y ancho de las graficas

plt.subplots_adjust(wspace=0.3, hspace=0.3)

plt.show()

#Graficos

import matplotlib.pyplot as plt

#Grafica simple 

x=[0,1,2,3,4,5,6,7,8,9,10]
y=[0,1,2,3,4,5,6,7,8,9,10]

plt.plot(x,y) #Crea el plot
plt.scatter(x,y) #Puntos de interseccion
plt.xlabel("Eje X") #Etiqueta eje X
plt.xlabel("Eje Y") #Etiqueta eje Y
plt.title("Mi primera grafica") #Titulo de la grafica 
plt.show()

#Grafico de barrar

x=[0,1,2,3,4,5,6,7,8,9,10]
y=[0,1,2,3,4,5,6,7,8,9,10]

plt.bar(x,y) #Crea el plot
plt.xlabel("Eje X") #Etiqueta eje X
plt.xlabel("Eje Y") #Etiqueta eje Y
plt.title("Mi primera grafica de barras") #Titulo de la grafica 
plt.show()

#GGPLOT

plt.style.use("ggplot")
print(plt.style.available)

x=[0,1,5,6,2,5,6,7,8,11,12]
y=[0,1,3,4,3,5,7,8,10,9,10]

plt.plot(x,y, color="blue", linestyle="--", marker="o")
plt.xlabel("Valores medidos")
plt.ylabel("Tiempo")
plt.show()
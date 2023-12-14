import pandas as pd

#Agrupar datos o SEGMENTACIÓN, AGREGAR DATOS, AGREGACION MULTINIVEL
data={"Nombre": ['Juan','Ana', 'Luis', 'Laura',' Pedro','Carla'],
      "Ciudad":[ 'Madrid', ' Barcelona' , 'Madrid', 'Valencia' , ' Barcelona','Madrid'],
      'Edad':[25, 33, 30, 28, 45, 38],
      "Puntuacion":[80,90,85,88,75,91]}

df=pd.DataFrame(data=data)
print(df)

#Agrupar datos por ciudad

agrupacion=df.groupby("Ciudad")
print(agrupacion.groups)

# Mostrar nombres de personas por cada ciudad
for ciudad, grupo in agrupacion:
    print(f"Personas en {ciudad}:")
    print(grupo[['Nombre', 'Edad','Puntuacion']])
    print()
    
#Agrupar datos por datos agregados 

Datos_agregados=agrupacion.agg(
    {
        "Edad":"mean",
        "Puntuacion":"sum"
    }
)
print(Datos_agregados)

#Definir funcion de agregacion personalizada

def rango (series):
    return series.max()-series.min ()

Datos_agregados_2=agrupacion.agg(
    {
        "Edad":rango,
        "Puntuacion":rango
    }
)

print(Datos_agregados_2)

data["Categoria"]=["A","B","A","B","A","B"]
df=pd.DataFrame(data)
print(df)

#Agrupar datos por cuidad y categoria 

agrupacion_multi=df.groupby(["Ciudad","Categoria"])
print(agrupacion_multi.groups)

# Mostrar nombres y edades de personas por cada ciudad y categoría
for (ciudad, categoria), grupo in agrupacion_multi:
    print(f"Personas en {ciudad} - Categoría {categoria}:")
    print(grupo[['Nombre', 'Edad']])
    print()
    
#Calcular la suma de las edades y las medias de las puntuaciones 
Datos_agregados_mult=agrupacion_multi.agg(
    {
        "Edad":"mean",
        "Puntuacion":"sum"
    }
)
print(Datos_agregados_mult)

    
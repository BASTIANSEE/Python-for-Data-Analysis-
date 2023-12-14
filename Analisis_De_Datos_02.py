#Tratamientos de datos 
# Importar numpy 

from os import rename
import numpy as np 
import pandas as pd

#Diccionario

data={
    "Nombre":["Ana","Esteban","George","Eduardo","Sebastian"], 
    "Edad":[21,22,21,np.nan,22],
    "Ciudad":["Quito","Riobamba",None,"Quito","Loja"]
}
print(data)

#Diccionario a Dataframe

df=pd.DataFrame(data=data)
print(df)

#Limpieza de datos 
#Rellenar valores faltantes

df_fill = df.fillna(
{
    "Edad":df["Edad"].mean(),
    "Ciudad": "Desconocido"
}
)
print(df_fill)

#Eliminar filas de los valores faltantes

df_sin_nan=df.dropna()
print(df_sin_nan)

#Reemplazar valores especificos de una coloumna 

df_reem=df.replace(
    {
        "Ciudad":{None:"Desconocido"}
    }
)
print(df_reem)

#Interpolar valores

df_interpolado= df.copy()
df_interpolado["Edad"]=df["Edad"].interpolate()
print(df_interpolado)

#Valores duplicados

data_duplicada={
    "Nombre":["Ana","Esteban","George","Eduardo","Sebastian","Ana","Eduardo"], 
    "Edad":[21,22,21,np.nan,22,21,np.nan],
    "Ciudad":["Quito","Riobamba",None,"Quito","Loja","Quito","Quito"]
}


df_duplicado=pd.DataFrame(data=data_duplicada)
print(df_duplicado)

df_sin_duplicados=df_duplicado.drop_duplicates()
print(df_sin_duplicados)

#Renombrar columnas

df_renobrado=df.rename(columns={"Nombre":"Name","Edad":"Age", "Ciudad":"City"})
print(df_renobrado)

#Ordenar columnas

Columnas_ordenadas=["Ciudad", "Edad", "Nombre"]
df_ordenado=df[Columnas_ordenadas]
print(df_ordenado)

#Transformación de datos 

def cuadrado (x):
    return x**2
df["Edad_Cuadrado"]=df["Edad"].apply(cuadrado)
print(df)
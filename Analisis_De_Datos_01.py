#Dataframes, Importar, Exportar, Filtrar

import pandas as pd 

#Series de PANDAS

numero= [1,2,3,4,5,6,7]
serie=pd.Series(numero)
print(serie)

#Diccionario

data={
    "Nombre":["Ana","Esteban","George","Eduardo","Sebastian"], 
    "Edad":[21,22,21,23,22],
    "Ciudad":["Quito","Riobamba","Ambato","Quito","Loja"]
}
print(data)

#Diccionario a Dataframe

df=pd.DataFrame(data=data)
print(df)

#Exportar dataframe

df.to_csv("data.csv")

#Importar dataframe

import_df=pd.read_csv("data.csv", index_col=0)

#Seleccionar una columna

nombres=df["Nombre"]
print(nombres)

#Seleccionar dos o más columnas

nom_ciu=df[["Nombre", "Ciudad"]]
print(nom_ciu)

#Filtrar por indice

fila=df.loc[2]
print(fila)

#Filtrar por condiciones

Mayores=df[df["Edad"]>22]
print(Mayores)

#Doble filtro

Filtro_doble=(df["Edad"]>20)&(df["Nombre"].str.startswith("A"))
print(df[Filtro_doble])

#Filtar por Query 

Filtro_query=df.query("Edad>21")
print(Filtro_query)

#Filtrar por isin

Filtro_isin=df[df["Nombre"].isin(["Ana","Sebastian"])]
print(Filtro_isin)

#Filtrar por funcion 

def longitud_7(nombre):
    return len(nombre)==7

print(df[df["Nombre"].apply(longitud_7)])

#Filtrar por rango

print(df[df["Edad"].between(21,23)])


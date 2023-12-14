import pandas as pd
#Agregar datos nuevos a un data frame, combinar datos de dataframes

data={"Nombre": ['Juan','Ana', 'Luis', 'Laura',' Pedro','Carla'],
      "Ciudad":[ 'Madrid', ' Barcelona' , 'Madrid', 'Valencia' , ' Barcelona','Madrid']}

df=pd.DataFrame(data=data)
print(df)

#Agregar nueva columna 

df["Edad"]=[21,20,19,23,21,22]
print(df)

#Generamos nueva fila

new_row = pd.Series({"Nombre":"Alex","Ciudad":"Madrid","Edad":22})

#Agregamos fila 

df=pd.concat([df, new_row.to_frame().T], ignore_index=True)
print(df)

#Combinar dataframes

data1={"Nombre": ['Juan','Ana', 'Luis', 'Laura',' Pedro','Carla'],
      "Edad":[21,23,22,19,20,21],
      "Ciudad":[ 'Madrid', ' Barcelona' , 'Madrid', 'Valencia' , ' Barcelona','Madrid']}

data2={"Nombre": ['Mateo','Anastacia', 'Ray', 'Mario',' Eduardo','Cali'],
      "Edad":[21,23,22,19,20,21],
      "Ciudad":[ 'Madrid', ' Barcelona' , 'Madrid', 'Valencia' , ' Barcelona','Madrid']}

df1=pd.DataFrame(data=data1)
print(df1)

df2=pd.DataFrame(data=data2)
print(df2)

df_combined=pd.concat([df1,df2], ignore_index=True)
print(df_combined)
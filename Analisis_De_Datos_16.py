import seaborn as sns
#CORRELACIÓN DE PEARSON 
from scipy.stats import pearsonr

## Sirve para ver que variable se correlaciona con otras y poder hacer reduccion de variables, predicciones, etc
## La correlación no implica causalidad, se necesita más pruebas 

df=sns.load_dataset("iris")
print(df)

#Calcular la correlacion de Pearson 

Correlacion, _=pearsonr(df["sepal_length"],df["petal_length"])
print(f"La correlación de Pearson entre sepal_length y petal_length es:{Correlacion} ")
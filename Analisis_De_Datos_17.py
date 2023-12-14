# Técnica Analisis de Clusters
import seaborn as sns 
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt

#Intenta separar aquellos elementos muy parecidos pero que no lo son 

df=sns.load_dataset("iris")
print(df)

model=KMeans(n_clusters=3, random_state=42)
df["cluster"]=model.fit_predict(df.iloc[:,:-1])

print(df)

sns.scatterplot(data=df, x="sepal_width", y="petal_length", hue="cluster")
plt.show()

#El modelo tiende a confundise o equivocase se puede solucionar con ML
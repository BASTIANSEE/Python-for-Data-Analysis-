import numpy as np

#Crear arreglo de una dimension con 5 elementos 

arr1= np.array([1,2,3,4,5,6])
print("Arreglo 1D", arr1)
print("Forma (Shape)", arr1.shape)
print("Tipo de dato",arr1.dtype)

#Cambiar el arreglo a una matriz 3x2

arr2= arr1.reshape((2,3))
print("Arreglo 2D\n", arr2)
print("Forma (Shape)", arr2.shape)
print("Tipo de dato",arr2.dtype)

#Crear una matrix de 4x4 con numeros aleatorios

matrix=np.random.rand(4,4)
print("Arreglo 4D\n", matrix)
print("Forma (Shape)", matrix.shape)
print("Tipo de dato",matrix.dtype)

#Crear un arreglo a partir de 2 dim a partir de listas de listas

arr=np.array([[1,2,3],[1,2,4],[2,3,4]])
print(arr)

#Crear un arreglo 3x4 de ceros

arr=np.zeros([3,4])
print(arr)

#Crear un arreglo 3x4 de unos

arr=np.ones([3,4])
print(arr)

#Acceder a elementos y modificar

arr[1,1]=10
print(arr)

#Crear matriz identidad
arr=np.eye(4)
print(arr)

#Crear un array 3d de cero con forma (2,3,4)

arr=np.zeros((4,3,4))
print(arr)

#Crear un array 2x2 aleatoria

arr=np.random.rand(2,5)
print(arr)

#Transponer 

print(arr.T)

#Unir horizontal

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
print(arr1,arr2)

arr_H=np.hstack((arr1,arr2))
print(arr_H)

#Unir Verticalmente

arr_v=np.vstack((arr1,arr2))
print(arr_v)

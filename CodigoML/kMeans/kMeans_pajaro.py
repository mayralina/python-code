#importar modulos/librerias
import numpy as np  #libreria para formato de numeros
import pandas as pd #libreria para cargar o llamar datos
import matplotlib.pyplot as plt  #libreria para hacer graficas
import seaborn as sb  #libreria para graficas
from scipy.io import loadmat
#matplotlib inline


#Inicializar centroides aleatoriamente
def init_centroids(X, k):
    m, n = X.shape
    centroids = np.zeros((k, n))
    idx = np.random.randint(0, m, k)
    
    for i in range(k):
        centroids[i,:] = X[idx[i],:]
    
    return centroids

#funcion para estimar los centroides de cada cluster
def find_closest_centroids(X, centroids):
    m = X.shape[0]
    k = centroids.shape[0]
    idx = np.zeros(m)
    
    for i in range(m):
        min_dist = 1000000
        for j in range(k):
            dist = np.sum((X[i,:] - centroids[j,:]) ** 2)
            if dist < min_dist:
                min_dist = dist
                idx[i] = j
    
    return idx

#Necesitamos una funcion para calcular el centroide de un cluster, el centroide es simplemente
#la media de los centroide asignados al cluster
def compute_centroids(X, idx, k):
    m, n = X.shape
    centroids = np.zeros((k, n))
    
    for i in range(k):
        indices = np.where(idx == i)
        centroids[i,:] = (np.sum(X[indices,:], axis=1) / len(indices[0])).ravel()
    
    return centroids

#Escribimos una funcion para correr el algoritmo:
#Lo unico que necesitamos hacer es alternar entre asignar centroides de prueba y re-calcular los centroides
def run_k_means(X, initial_centroids, max_iters):
    m, n = X.shape
    k = initial_centroids.shape[0]
    idx = np.zeros(m)
    centroids = initial_centroids
    
    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, k)
    
    return idx, centroids


#Carguemos la imagen
data_imagen = loadmat('data/bird_small_kmeans.mat')
A = data_imagen['A']
A.shape


# Normalicemos los rangos de los valores
A = A / 255.

# reshape el arreglo
X = np.reshape(A, (A.shape[0] * A.shape[1], A.shape[2]))

# Iniciar los centroides aleatoriamente
initial_centroids = init_centroids(X, 16)

#Correr el algoritmo
idx, centroids = run_k_means(X, initial_centroids, 10)

# Obtener los centroides mas cercanos una vez mas
idx = find_closest_centroids(X, centroids)

#mapear cada pixel al valor del centroide
X_recovered = centroids[idx.astype(int),:]

#Recambiar a las dimensiones originales
X_recovered = np.reshape(X_recovered, (A.shape[0], A.shape[1], A.shape[2]))

plt.imshow(X_recovered)
plt.savefig('pajaro_chico.png')


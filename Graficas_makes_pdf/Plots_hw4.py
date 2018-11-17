
# coding: utf-8

# In[35]:


# Importo lo que necesito para grafiar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[36]:


# Para graficar los datos del punto 2, la ecuacion diferencial ordinaria
#inicialmente se importan los datos generados por el programa de c++
#Esta primera parte consiste en la grafica de los datos de angulo de 45 grados
data = np.genfromtxt("datos1_ODE.dat",dtype=None,delimiter="\n")
tiempo=np.zeros([len(data)])
distancia_x=np.zeros([len(data)])
distancia_y=np.zeros([len(data)])
velocidad_x=np.zeros([len(data)])
velocidad_y=np.zeros([len(data)])
angulo = data[0].decode("UTF8").split(":")[1]
for i in range(1,len(data)):  
    tiempo[i] = float((data[i]).decode("UTF8").split(",")[0].split("=")[1])
    distancia_x[i] = float((data[i]).decode("UTF8").split(",")[1].split("=")[1])
    distancia_y[i] = float((data[i]).decode("UTF8").split(",")[2].split("=")[1])
    velocidad_x[i] = float((data[i]).decode("UTF8").split(",")[3].split("=")[1])
    velocidad_y[i] = float((data[i]).decode("UTF8").split(",")[4].split("=")[1])


# In[37]:


#Ahora se genera la grafica con los valores anteriores
plt.figure()
plt.plot(distancia_x,distancia_y,label="Angulo"+angulo)
plt.title("Grafica del movimiento del proyectil a 45 grados")
plt.ylabel("Distancia Y")
plt.xlabel("distancia X")
plt.grid(True)
plt.legend()
plt.savefig("ODE_45grados.pdf",bbox_inches="tight")


# In[40]:


#Ahora se vuelven a cargar los datos de ODE pero para la variacion de los angulos 
datos = np.genfromtxt("datos2_ODE.dat",dtype=None,delimiter="\n",skip_footer=1)
contadores = np.genfromtxt("datos2_ODE.dat",delimiter=",",skip_header=len(datos))
matrizDatos = []
inicioContador = 1;
finalContador = int(contadores[0]);
for i in range(7):
    matrizDatos.append([])
    for j in range(5):
        matrizDatos[i].append(np.zeros([int(contadores[i])-1]))
    for j in range(inicioContador,finalContador):
        matrizDatos[i][0][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[0].split("=")[1])
        matrizDatos[i][1][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[1].split("=")[1])
        matrizDatos[i][2][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[2].split("=")[1])
        matrizDatos[i][3][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[3].split("=")[1])
        matrizDatos[i][4][j-inicioContador] = float((datos[j]).decode("UTF8").split(",")[4].split("=")[1])
    inicioContador += int(contadores[i]);
    if i != 6:
        finalContador += int(contadores[i+1]);


# In[42]:


#Se grafican las distancias con la vaariacionn de los angulos entre 10 y 70
plt.figure()
for i in range(7):
    plt.plot(valores[i][1],valores[i][2],label="Angulo:"+str(10*(i+1)))
plt.title("Grafica del movimiento del proyectil a 45 grados")
plt.ylabel("Distancia Y")
plt.xlabel("distancia X")
plt.grid(True)
plt.legend()
plt.savefig("ODE_varicion_grados.pdf",bbox_inches="tight")


# In[ ]:





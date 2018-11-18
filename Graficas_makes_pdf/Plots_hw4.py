
# coding: utf-8

# In[56]:


# Importo lo que necesito para grafiar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[57]:


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


# In[58]:


#Ahora se genera la grafica con los valores anteriores
plt.figure()
plt.plot(distancia_x,distancia_y,label="Angulo"+angulo)
plt.title("Grafica del movimiento del proyectil a 45 grados")
plt.ylabel("Distancia Y")
plt.xlabel("distancia X")
plt.grid(True)
plt.legend()
plt.savefig("ODE_45grados.pdf",bbox_inches="tight")


# In[59]:


#Ahora se vuelven a cargar los datos de ODE pero para la variacion de los angulos 
datos2 = np.genfromtxt("datos2_ODE.dat",dtype=None,delimiter="\n",skip_footer=1)
data_count = np.genfromtxt("datos2_ODE.dat",delimiter=",",skip_header=len(datos2))
valores = []
data_count0 = 1;
data_countf = int(data_count[0]);
for i in range(7):
    valores.append([])
    for j in range(5):
        valores[i].append(np.zeros([int(data_count[i])-1]))
    for j in range(data_count0 ,data_countf):
        valores[i][0][j-data_count0] = float((datos2[j]).decode("UTF8").split(",")[0].split("=")[1])
        valores[i][1][j-data_count0] = float((datos2[j]).decode("UTF8").split(",")[1].split("=")[1])
        valores[i][2][j-data_count0] = float((datos2[j]).decode("UTF8").split(",")[2].split("=")[1])
        valores[i][3][j-data_count0] = float((datos2[j]).decode("UTF8").split(",")[3].split("=")[1])
        valores[i][4][j-data_count0] = float((datos2[j]).decode("UTF8").split(",")[4].split("=")[1])
    data_count0 += int(data_count[i]);
    if i != 6:
        data_countf += int(data_count[i+1]);


# In[60]:


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


# In[61]:


# Para graficar los datos del punto 3, la ecuacion diferencial parcial
#inicialmente se importan los datos generados por el programa de c++
#los datos son muy pesados asi que todo es muuuuy lento.


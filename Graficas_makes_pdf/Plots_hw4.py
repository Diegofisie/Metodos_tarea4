
# Importo lo que necesito para grafiar
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
#Ahora se genera la grafica con los valores anteriores
plt.figure()
plt.plot(distancia_x,distancia_y,label="Angulo"+angulo)
plt.title("Grafica del movimiento del proyectil a 45 grados")
plt.ylabel("Distancia Y")
plt.xlabel("distancia X")
plt.grid(True)
plt.legend()
plt.savefig("ODE_45grados.pdf",bbox_inches="tight")
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
# Para graficar los datos del punto 3, la ecuacion diferencial parcial
#inicialmente se importan los datos generados por el programa de c++
#los datos son muy pesados asi que todo es muuuuy lento.
data = np.genfromtxt("parte1_PDE.dat",None,skip_header=1)
tags = (np.genfromtxt("parte1_PDE.dat",skip_footer=(len(data)-1),dtype=None))[0].decode("UTF8").split(",")
#datos de variacion de temperatura en el tiempo
var_temp_tiempo = [] 
#tiempo del proceso
tiempo = int(tags[1])
#numero de "iteraciones" que se harian
N = int(tags[3])
N_0 = 1;
N_f = N+1

for i in range(tiempo):
    var_temp = np.zeros([N,N]) 
    for j in range(N_0,N_f):
        tag_data = data[j].decode("UTF8").split(",")
        for k in range(N):
            var_temp[j-N_0][k]=float(tag_data[k])
    N_0 += N+1
    N_f += N+1
    var_temp_tiempo.append(var_temp)
    
x = np.arange(0,N,1)
y = np.arange(0,N,1)
x,y = np.meshgrid(x, y)
#Temperatura en condiciones iniciales, es decir en el tiempo inicial
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo[0], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_10gc1.pdf",bbox_inches="tight")
#Grafica de temperatura para tiempo 2*tiempo/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo[int((tiempo-1)*2/3)], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_10gc2.pdf",bbox_inches="tight")
#Grafica de temperatura para tiempo tiempo/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo[int((tiempo-1)/3)], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_10gc3.pdf",bbox_inches="tight")
#Grafica de temperatura para tiempo 1
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo[int((tiempo-1))], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_10gc4.pdf",bbox_inches="tight")


# In[12]:


# Para graficar los datos del punto 3, la ecuacion diferencial parcial
#inicialmente se importan los datos generados por el programa de c++
#los datos son muy pesados asi que todo es muuuuy lento.
#SE importan los datos de la parte 2
data2 = np.genfromtxt("parte2_PDE.dat",None,skip_header=1)
tags2 = (np.genfromtxt("parte2_PDE.dat",skip_footer=(len(data2)-1),dtype=None))[0].decode("UTF8").split(",")
#datos de variacion de temperatura en el tiempo
var_temp_tiempo2 = [] 
#tiempo del proceso
tiempo2 = int(tags2[1])
#numero de "iteraciones" que se harian
N2 = int(tags2[3])
N2_0 = 1;
N2_f = N2+1

for i in range(tiempo2):
    var_temp2 = np.zeros([N2,N2]) 
    for j in range(N2_0,N2_f):
        tag_data2 = data2[j].decode("UTF8").split(",")
        for k in range(N):
            var_temp2[j-N2_0][k]=float(tag_data2[k])
    N2_0 += N2+1
    N2_f += N2+1
    var_temp_tiempo2.append(var_temp2)
    
x = np.arange(0,N2,1)
y = np.arange(0,N2,1)
x,y = np.meshgrid(x, y)
#Temperatura en condiciones iniciales, es decir en el tiempo inicial
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo2[0], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_Abiertas1.pdf",bbox_inches="tight")




# In[16]:


#Grafica de temperatura para tiempo 2*tiempo/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo2[int((tiempo2-1)*2/3)], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_Abiertas2.pdf",bbox_inches="tight")

#Grafica de temperatura para tiempo tiempo/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo2[int((tiempo2-1)/3)], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_Abiertas3.pdf",bbox_inches="tight")

#Grafica de temperatura para tiempo 1
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo2[int(tiempo2-1)], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_Abiertas4.pdf",bbox_inches="tight")


# In[15]:


# Para graficar los datos del punto 3, la ecuacion diferencial parcial
#inicialmente se importan los datos generados por el programa de c++
#los datos son muy pesados asi que todo es muuuuy lento.
#SE importan los datos de la parte 3
data3 = np.genfromtxt("parte3_PDE.dat",None,skip_header=1)
tags3 = (np.genfromtxt("parte3_PDE.dat",skip_footer=(len(data3)-1),dtype=None))[0].decode("UTF8").split(",")
#datos de variacion de temperatura en el tiempo
var_temp_tiempo3 = [] 
#tiempo del proceso
tiempo3 = int(tags3[1])
#numero de "iteraciones" que se harian
N3 = int(tags3[3])
N3_0 = 1;
N3_f = N3+1

for i in range(tiempo3):
    var_temp3 = np.zeros([N3,N3]) 
    for j in range(N3_0,N3_f):
        tag_data3 = data3[j].decode("UTF8").split(",")
        for k in range(N3):
            var_temp3[j-N3_0][k]=float(tag_data3[k])
    N3_0 += N3+1
    N3_f += N3+1
    var_temp_tiempo3.append(var_temp3)
    
x = np.arange(0,N3,1)
y = np.arange(0,N3,1)
x,y = np.meshgrid(x, y)
#Temperatura en condiciones iniciales, es decir en el tiempo inicial
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo3[0], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_periodicas1.pdf",bbox_inches="tight")
#Grafica de temperatura para tiempo 2*tiempo/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo3[int((tiempo3-1)*2/3)], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_Periodicas2.pdf",bbox_inches="tight")

#Grafica de temperatura para tiempo tiempo/3
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo3[int((tiempo3-1)/3)], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_Periodicas3.pdf",bbox_inches="tight")

#Grafica de temperatura para tiempo 1
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, var_temp_tiempo3[int(tiempo3-1)], rstride=1, cstride=1, cmap='winter', linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
fig.savefig("PDE_temp_Periodicas4.pdf",bbox_inches="tight")


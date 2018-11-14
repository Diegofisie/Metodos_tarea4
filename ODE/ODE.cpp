/* En este ejercicio deben solucionar la ecuacion de movimiento de un proyectil para el caso en
que hay una friccion proporcional a v2. Deben escribir un codigo en c++ llamado ODE cpp donde implementen el 
metodo de Leap-Frog o el metodo de Runge Kutta de 4to orden para
resolver la ecuacon de movimiento:*/

//////Importo lo necesario//////
#include<iostream>
#include <vector>
#include <math.h> 
#include<cmath>
#include <vector>
using namespace std;
///// Se declaran las constantes necesarias para desarrollar la ecuacion//////
float static PI = 3.14159265359; // el valor de pi como una constante global 
vector<float> g; // la ecelerecion gravitacional en metros sobre segundo cuadrado
float static c = 0.2; // el coeficiente de friccion 
float static m  = 0.2; // la masa del objeto en kilo gramos
float static ht = 0.001; // variacion del tiempo entre cada instante
///// Se declaras las variables de la ecuacion que varian segun los puntos /////
float static tmax = 2.0; //el tiempo maximo con el que se trabajara
int N = (int) tmax/ht; // el numero de iteraciones que se realizaran en el sisema
vector<float> f[2];

/* Se define la funcion con la cual se construira la ecuacion a esta funcion 
le entran por parameto las 2 componentes de un vector v*/
void calcularFuncion(vector<float> v0,vector<float> v1){
	float magv1 = sqrt(pow(v1.at(0),2)+pow(v1.at(1),2));
	vector<float> tempv1;
	float tempv1_x = -g.at(0)-(c/m)*(magv1)*v1.at(0);
	float tempv1_y = -g.at(1)-(c/m)*(magv1)*v1.at(1);
	tempv1.push_back(tempv1_x);
	tempv1.push_back(tempv1_y);
	f[0]=v1;
	f[1]=tempv1;
}

/*Se define la funcion con la cual se resolvera la ecuacion para encontrar el movimiento
del proyectil utilizando el metodo de Rugen Kuta 4*/











int main() {

    
  return 0;
}
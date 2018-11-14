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








int main() {
    
  return 0;
}
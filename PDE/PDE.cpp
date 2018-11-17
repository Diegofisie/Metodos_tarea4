//En este ejercicio deben solucionar la ecuacion de difusion en 2 dimensiones.
/*Suponga que tiene una varilla metalica de 10 cm de diametro que esta entre una roca. Suponga
que la roca es una calcita con coeciente de difusion v = k/(Cp*rho) ) donde k = 1.62 m2s-1
es la conductividad termica, Cp = 820Jkg-1K-1 es el calor especufico y rho = 2.71gcm-3 es la
densidad.*/

//Importo lo necesario para resolver el ejercicio 
#include<iostream>
#include <fstream>
#include <sstream>
#include <math.h> 
#include<cmath>

using namespace std;

// Se declaran las constantes necesarias y que se utilizaran en el ejercicio para resolver la eqn
static float L = 50.0; // Se asume que la longitud de la varilla es de 50 cm por la eespecicicacion
//de la roca que es de 50 x 50 centimetros
static float d = 10.0; //EL diametro de la varilla metalica 
static float k_d = 1.62; // la conductividad termica de la ecuacion de coeff de difusion 
static float Cp = 820; // el calor especifico para la ecuacion de coeff de difusion  
static float rho = 2710; // la densidad para la ecuacion del coeff de difusion
static float v = k_d/(Cp*rho); //ecuacion del coeficiente de difusion, utilizando las cts anteriores
static float dx = 1; // variacion de x para la ecuacion que es igual a la variacion en y
static float alpha = 0.2;	
static float dt = alpha*pow(dx,2)/v;
int Num = (int) L/dx; // el numero de pasos que se tomaran para analizar los datos 
int Num_varilla = (int) d/dx; // lo mismo que para el anterior pero con el diametro de la varilla 
int Temp_10gc = 1000;
int Temp_open = 1000;
int Temp_peri = 1000;



/*Se procede con la contruccion de las funciones para resolver la ecuacion, incialmente la primera 
funcion es la encargada de contruir las condicones de frontera que se establecen en el enunciado del
problema. La primera de las funciones establece las condiciones de frontera fijas a 10 grados centigrados
esta funcion tiene un unico parametro y es el nombre del archivo donde se busca guardar los datos generados
al resulver la ecuacion de difusion*/
void eqn_dif_10gc(string nombre_txt){
	//se genera el archivo de texto con el nombre escrito para guardar los datos de las ecuaciones
	ofstream file;
	file.open(nombre_txt.c_str());
	// Se generan matrices las cuales almacenaran los dato obtenidos por la solcuion de la ecuacion
	float datos_anteriores[Num][Num];
	float datos_actuales[Num][Num];
	// Se crea un for para asignar las condiciones de frontera de la varilla como 10 y el resto de ella 100
	for (int i = 0; i < Num; ++i)
	{
		for (int j = 0; j < Num; ++j)
		{	
			float eqn_calculo = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
			if (eqn_calculo <= pow(d/2,2))
			{
				datos_anteriores[i][j]=100;
			}
			else{
				datos_anteriores[i][j]=10;
			}
		}
	}
	// Se escribe en el archivo de datos creado la temperatura de la varilla para verifiar que se haya creado
	file << "Temperatura,"<<Temp_10gc<<",Num"<<Num<<"\n";
	// Ahora se crea el for para la solucion de la ecuacion diferencial parcial
	for (int k = 0; k < Temp_10gc; ++k)
	{
		file << "Tiempo:"<<k*dt<<"\n";
		for (int i = 0; i < Num; ++i)
		{
			for (int j = 0; j < Num; ++j)
			{	
				if ((i > 0  && i < (Num-1)) && (j > 0 && j < (Num-1)))
				{
					float eqn_calculo = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
					if (eqn_calculo > pow(d/2,2))
					{
						//Para resolver la ecuacion se usa el mismo concepto que usamos en clase para resolver la eqn de calor
						datos_actuales[i][j]=alpha*(datos_anteriores[i+1][j]+datos_anteriores[i-1][j]+datos_anteriores[i][j+1]+datos_anteriores[i][j-1])+((1-4*alpha)*datos_anteriores[i][j]);
					}
					else{
						datos_actuales[i][j] = 100;
					}
				}
				else{
					datos_actuales[i][j] = 10;
				}
				file << datos_anteriores[i][j]<< ",";
			}
			file << "\n";
		}
		// Se asigna el paso siguinte al sistema para que este vuelva a empezar y genere todos los resultados.
		for (int i = 0; i < Num; ++i)
		{
			for (int j = 0; j < Num; ++j)
			{
				datos_anteriores[i][j]=datos_actuales[i][j];
			}
		}
	}
	file.close();
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*Generados los datos con la funcion para las ecuaciones de fronte de 10 grados centigrados se procede con la 
segunda parte la cual es realizar la solucion de la ecuacion con condiciones de frontera abiertas*/
void eqn_dif_open(string nombre_txt){
	//Creacion archivo de datos
	ofstream file;
	file.open(nombre_txt.c_str());

	float datos_anteriores[Num][Num];
	float datos_actuales[Num][Num];

	for (int i = 0; i < Num; ++i)
	{
		for (int j = 0; j < Num; ++j)
		{
			float eqn_calculo = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
			if (eqn_calculo <= pow(d/2,2))
			{
				datos_anteriores[i][j]=100;
			}
			else{
				datos_actuales[i][j]=10;
			}
		}
	}
	file << "T,"<<Temp_open<<",N,"<<Num<<"\n";



	for (int k = 0; k < Temp_open; ++k)
	{
		file << "Tiempo:"<<k*dt<<"\n";
		for (int i = 0; i < Num; ++i)
		{
			for (int j = 0; j < Num; ++j)
			{	
				if ((i > 0  && i < (Num-1)) && (j > 0 && j < (Num-1)))
				{
					float eqn_calculo = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
					if (eqn_calculo > pow(d/2,2))
					{
						//Para resolver la ecuacion se usa el mismo concepto que usamos en clase para resolver la eqn de calor
						datos_actuales[i][j]=alpha*(datos_anteriores[i+1][j]+datos_anteriores[i-1][j]+datos_anteriores[i][j+1]+datos_anteriores[i][j-1])+((1-4*alpha)*datos_anteriores[i][j]);
					}
					else{
						datos_actuales[i][j] = 100;
					}
				}
				else{
					for (int i = 0; i < Num; ++i)
					{
						datos_actuales[0][i]=datos_actuales[1][i];
						datos_actuales[Num-1][i]=datos_actuales[Num-2][i];
						datos_actuales[i][0]=datos_actuales[i][1];
						datos_actuales[i][Num-1]=datos_actuales[i][Num-2];
					}
				}
				file<< datos_anteriores[i][j]<< ",";
			}
			file << "\n";
		}
		for (int i = 0; i < Num; ++i)
		{
			for (int j = 0; j < Num; ++j)
			{
				datos_anteriores[i][j]=datos_actuales[i][j];
			}
		}
	}
	file.close();
}
/*Generados los datos con la funcion para las ecuaciones de frontera de 10 grados centigrados y con condiciones
abiertas se procede con la tercera la cual es realizar la solucion de la ecuacion con condiciones de frontera
periodicas*/
void eqn_dif_peri(string nombre_txt){
	//Creacion archivo de datos
	ofstream file;
	file.open(nombre_txt.c_str());

	float datos_anteriores[Num][Num];
	float datos_actuales[Num][Num];

	for (int i = 0; i < Num; ++i)
	{
		for (int j = 0; j < Num; ++j)
		{
			float eqn_calculo = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
			if (eqn_calculo <= pow(d/2,2))
			{
				datos_anteriores[i][j]=100;
			}
			else{
				datos_actuales[i][j]=10;
			}
		}
	}
	file << "T,"<<Temp_peri<<",N,"<<Num<<"\n";
	for (int k = 0; k < Temp_peri; ++k)
	{
		file << "Tiempo:"<<k*dt<<"\n";
		for (int i = 0; i < Num; ++i)
		{
			for (int j = 0; j < Num; ++j)
			{	
				if ((i > 0  && i < (Num-1)) && (j > 0 && j < (Num-1)))
				{
					float eqn_calculo = pow((i*dx)-(L/2),2)+pow((j*dx)-(L/2),2);
					if (eqn_calculo > pow(d/2,2))
					{
						datos_actuales[i][j]=alpha*(datos_anteriores[i+1][j]+datos_anteriores[i-1][j]+datos_anteriores[i][j+1]+datos_anteriores[i][j-1])+((1-4*alpha)*datos_anteriores[i][j]);
					}
					else{
						datos_actuales[i][j] = 100;
					}
				}
				else{
					for (int i = 0; i < Num; ++i)
					{
						datos_actuales[0][i]=datos_actuales[Num-1][i];
						datos_actuales[i][0]=datos_actuales[i][Num-1];
					}
				}
				file << datos_anteriores[i][j]<< ",";
			}
			file << "\n";
		}
		for (int i = 0; i < Num; ++i)
		{
			for (int j = 0; j < Num; ++j)
			{
				datos_anteriores[i][j]=datos_actuales[i][j];
			}
		}
	}
	file.close();
}









int main(){
	eqn_dif_10gc("parte1_PDE.dat");
	eqn_dif_open("parte2_PDE.dat");
	eqn_dif_peri("parte3_PDE.dat");
	return 0;
}
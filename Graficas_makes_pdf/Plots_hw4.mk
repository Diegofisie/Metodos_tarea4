Resultados_hw4.pdf: Resultados_hw4.tex ODE_45grados.pdf
	pdflatex Resultados_hw4.tex
	rm Resultados_hw4.log
	rm Resultados_hw4.aux
	rm ODE_45grados.pdf ODE_varicion_grados.pdf PDE_temp_10gc1.pdf PDE_temp_Abiertas1.pdf PDE_temp_periodicas1.pdf PDE_temp_10gc2.pdf PDE_temp_Abiertas2.pdf PDE_temp_Periodicas2.pdf PDE_temp_10gc3.pdf PDE_temp_Abiertas3.pdf PDE_temp_Periodicas3.pdf PDE_temp_10gc4.pdf PDE_temp_Abiertas4.pdf PDE_temp_Periodicas4.pdf	
ODE_45grados.pdf: datos1_ODE.dat parte1_PDE.dat
	python Plots_hw4.py
	rm datos1_ODE.dat datos2_ODE.dat datos3_ODE.dat parte1_PDE.dat parte2_PDE.dat parte3_PDE.dat

datos1_ODE.dat: ODE.cpp
	g++ ODE.cpp
	./a.out
	rm a.out

parte1_PDE.dat: PDE.cpp
	g++ PDE.cpp
	./a.out
	rm a.out
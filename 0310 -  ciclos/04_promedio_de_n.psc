Algoritmo promedio_de_n
	Escribir "Este programa saca el promedio de los números que ingreses"
	
	promedio <- 0
	num <- 1
	contador <- 0
	
	Mientras num <> 0 Hacer
		Escribir "Ingresa un número o 0 para salir: " Sin Saltar
		Leer num
		promedio <- promedio + num
		contador <- contador + 1
	Fin Mientras
	
	promedio <- promedio / contador
	Escribir "El promedio es: ", promedio
	
FinAlgoritmo

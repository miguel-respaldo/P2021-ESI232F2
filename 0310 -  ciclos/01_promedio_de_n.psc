Algoritmo promedio_de_n
	
	Escribir "¿Cuantos numeros quieres promediar?:" Sin Saltar
	Leer cantidad
	
	promedio <- 0
	
	Para i<-1 Hasta cantidad Con Paso 1 Hacer
		Escribir "Introduce un número: " Sin Saltar
		Leer num
		promedio <- promedio + num
	Fin Para
	
	promedio <- promedio / cantidad
	
	Escribir "El promedio fue: ", promedio
	
FinAlgoritmo

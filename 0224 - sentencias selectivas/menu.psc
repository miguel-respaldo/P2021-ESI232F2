Algoritmo menu
	// Realizar  4 operaciones  aritméticas:  suma, resta, multiplicación
	// y división,  con dos números enteros. 
	// Elegir una de las opciones y realizar  el calculo correspondiente. 
	
	// Pido los números
	Escribir "Escribe un número: " Sin Saltar
	Leer num1
	Escribir "Escribe otro número: " Sin Saltar
	Leer num2
	
	// Mostramos el menu
	Escribir "1. Suma"
	Escribir "2. Resta"
	Escribir "3. Multiplicación"
	Escribir "4. División"
	Escribir ""
	Escribir "Opción: " Sin Saltar
	Leer op
	
	// Seleccióno la opción segun la operación
	Segun op Hacer
		1:
			Escribir "La suma es: ", num1 + num2
		2:
			resultado = num1 - num2
			Escribir "La resta es: ", resultado
		3:
			Escribir "La multiplicación es: ", num1 * num2
		4:
			Si num2 = 0 Entonces
				Escribir "No se puede dividir entre 0"
			SiNo
				resultado = num1 / num2
				Escribir "La división es: ", resultado	
			FinSi						
		De Otro Modo:
			Escribir "Opción invalida."
	Fin Segun
	
	
FinAlgoritmo

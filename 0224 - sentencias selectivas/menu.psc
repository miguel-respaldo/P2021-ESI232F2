Algoritmo menu
	// Realizar  4 operaciones  aritm�ticas:  suma, resta, multiplicaci�n
	// y divisi�n,  con dos n�meros enteros. 
	// Elegir una de las opciones y realizar  el calculo correspondiente. 
	
	// Pido los n�meros
	Escribir "Escribe un n�mero: " Sin Saltar
	Leer num1
	Escribir "Escribe otro n�mero: " Sin Saltar
	Leer num2
	
	// Mostramos el menu
	Escribir "1. Suma"
	Escribir "2. Resta"
	Escribir "3. Multiplicaci�n"
	Escribir "4. Divisi�n"
	Escribir ""
	Escribir "Opci�n: " Sin Saltar
	Leer op
	
	// Selecci�no la opci�n segun la operaci�n
	Segun op Hacer
		1:
			Escribir "La suma es: ", num1 + num2
		2:
			resultado = num1 - num2
			Escribir "La resta es: ", resultado
		3:
			Escribir "La multiplicaci�n es: ", num1 * num2
		4:
			Si num2 = 0 Entonces
				Escribir "No se puede dividir entre 0"
			SiNo
				resultado = num1 / num2
				Escribir "La divisi�n es: ", resultado	
			FinSi						
		De Otro Modo:
			Escribir "Opci�n invalida."
	Fin Segun
	
	
FinAlgoritmo

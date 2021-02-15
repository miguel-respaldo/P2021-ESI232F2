Algoritmo par_o_impar
	
	Escribir "Escribe un número: " Sin Saltar
	Leer num
	
	Escribir "El resultado del modulo es: ",   num mod 2
	Escribir "El resultado de la division es: ",num / 2
	
	//Si num % 2 = 0 Entonces
	Si num mod 2 = 0 Entonces
		Escribir "El número es par"
	SiNo
		Escribir "El número es impar"
	Fin Si
	
FinAlgoritmo

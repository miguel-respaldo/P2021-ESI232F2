Algoritmo compras
	// Comprar 4 productos (tele, compu, refri, cel) 
	// tele  si 10% < 5000 < 20%
	// compu si 10% < 15000 < 20%
	// refri si 10% < 10000 < 20%
	// cel   si 10% < 8000 < 20%
		
	Escribir "1. tele"
	Escribir "2. compu"
	Escribir "3. refri"
	Escribir "4. cel"
	Escribir "¿Que deseas comprar?: " Sin Saltar
	Leer producto
	Escribir "¿Cuanto cuesta?: " Sin Saltar
	Leer precio
	
	Segun producto Hacer
		1:
			Si precio > 5000 Entonces
				Escribir "Tienes un descuento de 20%"
				precio_final <- precio * 0.8				
			SiNo
				Escribir "Tienes un descuento de 10%"
				precio_final <- precio * 0.9
			Fin Si
			Escribir "El precio final es", precio_final
			
		2:
			Si precio > 15000 Entonces
				Escribir "Tienes un descuento de 20%"
				precio_final <- precio * 0.8
			SiNo
				Escribir "Tienes un descuento de 10%"
				precio_final <- precio * 0.9
			Fin Si
			Escribir "El precio final es", precio_final
		3:
			Si precio > 10000 Entonces
				Escribir "Tienes un descuento de 20%"
				precio_final <- precio * 0.8
			SiNo
				Escribir "Tienes un descuento de 10%"
				precio_final <- precio * 0.9
			Fin Si
			Escribir "El precio final es", precio_final
		4:
			Si precio > 8000 Entonces
				Escribir "Tienes un descuento de 20%"
				precio_final <- precio * 0.8
			SiNo
				Escribir "Tienes un descuento de 10%"
				precio_final <- precio * 0.9
			Fin Si
			Escribir "El precio final es", precio_final
		De Otro Modo:
			Escribir "El producto no existe"
	Fin Segun
FinAlgoritmo

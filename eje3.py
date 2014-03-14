iteraciones= int(raw_input('Cuantas interaciones? '))
entrada = raw_input('Que valor ')
while iteraciones > 0:
	iteraciones = iteraciones -1 
	entrada =str(int(entrada) + int(entrada[0]) + int(entrada[len(entrada)-1]))
	print entrada

	#entrada[int(1),1]
matriz=[1,1] #iniciamos la matriz con los elementos 1,1
iteraciones=int(raw_input('Cuantas series: ')) #Solicitamos la interaciones del ciclo
while iteraciones>0: #mientras interaciones no sea cero realiza lo siguiente
	iteraciones=iteraciones-1 # resta uno a interaciones
	indice=len(matriz) #calcula el largo (cantidadad de valores) de la matriz
	while indice>1: #mietras el indice sea mayor a uno
		indice=indice-1#resta uno al largo de la matriz por las posisones [0,1,...lenmatriz]
		matriz[indice]=matriz[indice]+matriz[indice-1] #suma los valores de matriz dejando libre la posisocon 0
	matriz.append(1)# agrega un uno al final de la matriz (en len(matriz))
	print matriz	
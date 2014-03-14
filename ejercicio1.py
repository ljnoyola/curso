print 'ESCRIBE UN VALOR ENTERO'
variable=0
while True:	
	entrada=raw_input()
	if entrada =='salir':
		break		
	variable=variable + int(entrada)
	print variable	
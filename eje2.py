variable=0
while True:	
	entrada=raw_input('que deseas hacer ')

	if entrada =='salir':
		break
	valor=raw_input('que valor ')		
	if entrada=='*':	
		variable=variable * int(valor)
	elif entrada=='/':		
		variable=variable / int(valor)
	elif entrada=='+':	
		variable=variable + int(valor)
	elif entrada=='-':		
		variable=variable - int(valor)
	print variable	
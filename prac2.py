#tupla=('gato',)
#print tupla

gato=(1,2,3,4)
perro="perro"

diccionario={'primero':gato,'segundo':'perro'}

if not gato:#len(gato) == len(perro):
	print "Entro al primer if"
elif len(gato) < len(perro):
	print "Entro al segundo if"
else:
	print "No entro al if"
#print diccionario ['primero']


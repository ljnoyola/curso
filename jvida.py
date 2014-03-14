import random
rango =3

def vecinos(x,y,matrix):
	x=0
	y=0
	contador = 0
	try:
		if matrix[y-1][x-1] == 'o':
			contador += 1
	except:
		pass
	try:
		if matrix[y-1][x] == 'o':
			contador += 1
	except:
		pass
	try:
		if matrix[y-1][x+1] == 'o':
			contador += 1
	except:
		pass
	try:
		if matrix[y][x-1] == 'o':
			contador += 1
	except:
		pass
	try:
		if matrix[y][x+1] == 'o':
			contador += 1
	except:
		pass
	try:
		if matrix[y+1][x-1] == 'o':
			contador += 1
	except:
		pass
	try:
		if matrix[y+1][x] == 'o':
			contador += 1
	except:
		pass
	try:
		if matrix[y+1][x+1] == 'o':
			contador += 1
	except:
		pass
	return contador

def llenado_matriz():
	if random.randrange(3) == 2:
		return 'o'
	else:
		return '.'


variable = 0

matrix=[[llenado_matriz() for x in xrange(rango)] for x in xrange(rango)]
for fila in matrix:	
	for imprime in fila:
		print imprime, 
	print



contador_filas = 0
while contador_filas < rango:
	contador_columnas = 0
	while contador_columnas < rango:
		vecinos(contador_columnas,contador_filas,matrix),
		contador_columnas += 1 
	print 
	contador_filas += 1








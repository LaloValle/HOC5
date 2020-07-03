from AnalizadorLexico import *
import AnalizadorSintactico as sintactico
from Programa import *

lexico = AnalizadorLexico()
lexico.construir()

sintactico.construir()

programa = Programa.programa()
while True:

	cadena = input('Cadena>> ')
	if cadena == 'exit': break
	print(lexico.analizarCadena(cadena))
	print('\n>>>>>>>>>>>>>>>>>>>>\n')
	sintactico.analizarCadena(cadena)
	#for i in range(len(programa._programa)):
	#	print('{} >> {}'.format(i,programa._programa[i]))
	
	programa.ejecutar()
	programa.reiniciarPrograma()
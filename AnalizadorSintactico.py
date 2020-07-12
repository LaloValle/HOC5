# -*- coding: utf-8 -*-
#@author: Lalo Valle

# Importacion del módulo de la implementación de yacc en python
import ply.yacc as yacc

from Programa import *
import Recursos as recursos

# Lista de nombres de los tokens
# Necesario para la generacion del parser
tokens = recursos.tokens
parser = None


programa = Programa.programa()

precedence = (
	('left', 'OR'),
	('left', 'AND'),
	('left', '>', 'MAYORIGUAL', '<', 'MENORIGUAL', 'IGUALREL', 'DIFERENTE'),
	('left', '+', '-'),
	('left', '*', '/','%'),
	('left', 'MENOSUNARIO','!'),
	('right', '^'),
	('left', 'INCREMENTO','DECREMENTO')
)

def p_lista(p):
	'''
	lista 	:
			| lista ';'
			| lista sentencia
	'''
	try:
		if len(p) == 2: p[0] = p[1]
		else: p[0] = p[2]
	except : pass

def p_lista_error(p):
	''' lista : lista error ';' '''
	recursos.imprimirError('ErrorSintaxis','Error de sintaxis en la regla lista. Expresión erronea')
	# Se agotan los token
	while True:
		if not parser.token(): break

def p_asignacion(p):
	'''	
	asignacion  : VARIABLE '=' expresion
				| INDEFINIDA '=' expresion
	'''
	p[0] = p[3]
	if p[1] not in recursos.variables: recursos.variables[p[1]] = None
	programa.agregarInstrucciones('varpush',p[1],'asignacion')

def p_asignacion_unidad(p):
	'''
	asignacion 	: VARIABLE INCREMENTO
				| VARIABLE DECREMENTO
	'''
	operador = p[2]
	p[0] = programa.agregarInstrucciones('varpush',p[1],'constpush',1)
	if operador == '++': programa.agregarInstrucciones('suma')
	else: programa.agregarInstrucciones('resta')
	programa.agregarInstrucciones('varpush',p[1],'asignacion')

def p_sentencia(p):
	''' sentencia 	: asignacion ';'
					| '{' listasentencias '}'
	'''
	if len(p) == 3: p[0] = p[1]
	else:
		programa.agregarInstrucciones('STOP') 
		p[0] = p[2]

def p_sentencia_print(p):
	''' sentencia : PRINT '(' expresion ')' ';' '''
	programa.agregarInstrucciones('print')
	p[0] = p[3]

def p_sentencia_while(p):
	'''	sentencia : while condicion sentencia termino'''
	p[0] = p[1]
	indiceInicioWhile = p[1]
	programa._programa[indiceInicioWhile + 1] = p[3]
	programa._programa[indiceInicioWhile + 2] = p[4]

def p_sentencia_if(p):
	''' sentencia 	: if condicion sentencia termino
					| if condicion sentencia termino ELSE sentencia termino
	'''
	p[0] = p[1]
	indiceInicioIf = p[1]
	programa._programa[indiceInicioIf + 1] = p[3]
	if len(p) == 8: 
		programa._programa[indiceInicioIf + 2] = p[6]
		programa._programa[indiceInicioIf + 3] = p[7]
	else: programa._programa[indiceInicioIf + 3] = p[4]





def p_sentencia_for(p):
	''' sentencia : for '(' listaasignaciones condicion listaexpresiones ')' sentencia termino '''
	#programa.agregarInstrucciones('STOP')   Se coloca el stop de la listaexpresiones
	p[0] = p[1]
	indiceInicioFor = p[1]
	programa._programa[indiceInicioFor + 1] = p[4]
	programa._programa[indiceInicioFor + 2] = p[5]
	programa._programa[indiceInicioFor + 3] = p[7]
	programa._programa[indiceInicioFor + 4] = p[8]

def p_listaasignaciones(p):
	'''
	listaasignaciones 	: 
						| siguiente
						| listaasignaciones
						| listaasignaciones asignacion coma siguiente
	'''
	if len(p) > 1:
		if len(p) == 2: p[0] = p[1]
		else: p[0] = p[2] if p[1] == None else p[1]

def p_listaexpresiones(p):
	'''
	listaexpresiones 	: 
						| siguiente
						| listaexpresiones
						| listaexpresiones expresion coma termino
	'''
	if len(p) > 1:
		if len(p) == 2: p[0] = p[1]
		else: p[0] = p[2] if p[1] == None else p[1]

def p_expresionlogica_constantes(p):
	'''
	expresionlogica : TRUE
					| FALSE
	'''
	p[0] = programa.agregarInstrucciones('constpush',p[1])

def p_expresionlogica_operaciones(p):
	'''
	expresionlogica : expresion '>' expresion
					| expresion MAYORIGUAL expresion
					| expresion '<' expresion
					| expresion MENORIGUAL expresion
					| expresion IGUALREL expresion
					| expresion DIFERENTE expresion
					| expresion AND expresion
					| expresion OR expresion
	'''
	p[0] = p[1]
	operador = p[2]
	if operador == '>': programa.agregarInstrucciones('mayorque')
	elif operador == '>=': programa.agregarInstrucciones('mayorigual')
	elif operador == '<': programa.agregarInstrucciones('menorque')
	elif operador == '<=': programa.agregarInstrucciones('menorigual')
	elif operador == '==': programa.agregarInstrucciones('igual')
	elif operador == '!=': programa.agregarInstrucciones('diferente')
	elif operador == '&&': programa.agregarInstrucciones('and')
	elif operador == '||': programa.agregarInstrucciones('or')

def p_siguiente(p):
	''' siguiente : ';' '''
	programa.agregarInstrucciones('STOP')
	p[0] = programa.getIndicePrograma()

def p_coma(p):
	'''
	coma 	:
			| ','
	'''
	p[0] = programa.getIndicePrograma()





def p_condicion(p):
	''' condicion 	: '(' expresionlogica ')' 
					|	expresionlogica ';'
	'''
	p[0] = p[2] if len(p) == 4 else p[1]
	programa.agregarInstrucciones('STOP')

def p_while(p):
	''' while : WHILE '''
	p[0] = programa.agregarInstrucciones('while')
	programa.agregarInstrucciones('STOP','STOP')

def p_if(p):
	''' if : IF '''
	p[0] = programa.agregarInstrucciones('if')
	programa.agregarInstrucciones('STOP','STOP','STOP')

def p_for(p):
	''' for : FOR '''
	p[0] = programa.agregarInstrucciones('for')
	programa.agregarInstrucciones('STOP','STOP','STOP','STOP')

def p_listasentencias(p):
	''' listasentencias :
						| listasentencias
						| listasentencias sentencia
	'''
	if len(p) > 1:
		if len(p) == 2: p[0] = p[1]
		else: p[0] = p[2] if p[1] == None else p[1]
	else: p[0] = programa.getIndicePrograma()


def p_expresion_constantes(p):
	''' 
	expresion 	: NUMERO 
				| CONSTANTE
				| CADENA
	'''
	p[0] = programa.agregarInstrucciones('constpush',p[1])

def p_expresion_variable(p):
	''' expresion : VARIABLE '''
	p[0] = programa.agregarInstrucciones('varpush',p[1])

def p_expresion_asignacion(p):
	''' expresion 	: asignacion 
					| expresionlogica
				  	| '(' expresion ')'
	'''
	p[0] = p[1] if len(p) == 2 else p[2]

def p_expresion_negaciones(p):
	''' expresion 	: '!' expresion
					| '-' expresion %prec MENOSUNARIO
	'''
	p[0] == p[2]
	if p[1] == '-': programa.agregarInstrucciones('negacion')
	else: programa.agregarInstrucciones('not')

def p_expresion_operaciones(p):
	''' expresion 	: FUNCION '(' expresion ')'
					| expresion '+' expresion
					| expresion '-' expresion
					| expresion '*' expresion
					| expresion '/' expresion
					| expresion '%' expresion
					| expresion '^' expresion
	'''
	if len(p) == 4: # Operaciones binarias
		p[0] = p[1]
		operador = p[2]
		if operador == '+': programa.agregarInstrucciones('suma')
		elif operador == '-': programa.agregarInstrucciones('resta')
		elif operador == '*': programa.agregarInstrucciones('multiplicacion')
		elif operador == '/': programa.agregarInstrucciones('division')
		elif operador == '%': programa.agregarInstrucciones('modulo')
		elif operador == '^': programa.agregarInstrucciones('potencia')
	else:  # Funciones
		p[0] = p[3]
		programa.agregarInstrucciones('funcion',p[1])

def p_termino(p):
	''' termino :'''
	programa.agregarInstrucciones('STOP')
	p[0] = programa.getIndicePrograma()

def p_error(p):
	if p:
		recursos.imprimirError('ErrorSintaxis','Error en el token {}'.format(p.type))
		# Descarta el token y prosigue con el proceso
		parser.errok()
	else:
		recursos.imprimirError('Error','Fin del entrada')


"""
	Funciones
	>>>>>>>>>
"""

def construir():
	global parser
	parser = yacc.yacc()

def analizarCadena(cadena):
	global parser
	parser.parse(cadena)
	programa.agregarInstrucciones('STOP')
	return programa._programa
# -*- coding: utf-8 -*-
#@author: Lalo Valle

import math

from Programa import *

programa = Programa.programa()

""" Lista de nombre de los tokens """
tokens = [
	'NUMERO',
	'INDEFINIDA',
	'VARIABLE',
	'FUNCION',
	'CONSTANTE',
	'CADENA',
	'PRINT',
	'OR',  # Operadores lógicos
	'AND',
	'MAYORIGUAL',
	'MENORIGUAL',
	'IGUALREL',
	'DIFERENTE',
	'WHILE',
	'IF',
	'ELSE',
	'FOR'
]
	
""" Tokens compuestos por unicamente un símbolo """
literals = [
	'+','-',
	'*','/','%',
	'^',
	'=',
	';',
	'(','{',
	')','}',
	'>','<',
	'!'
]


"""
	RECURSOS MATEMÁTICOS
	>>>>>>>>>>>>>>>>>>>>
"""
"""
	Funciones con validación de dominio
"""
def Log(x):
	try: return math.log(x)
	except Error: 
		mostrarError('ErrorLog :',Error)
		raise SyntaxError
	return None

def Log10(x):
	try: return math.log10(x)
	except Error: 
		mostrarError('ErrorLog10 :',Error)
		raise SyntaxError
	return None

def Exp(x):
	try: return math.exp(x)
	except Error: 
		mostrarError('ErrorExp :',Error)
		raise SyntaxError
	return None

def Sqrt(x):
	try: return math.sqrt(x)
	except Error: 
		mostrarError('ErrorSqrt',Error)
		raise SyntaxError
	return None

""" Diccionario de constantes matemáticas y su valor """
constantes = {
	'π':math.pi, 'PI':math.pi,
	'e':math.e, 'E':math.e,
	'Γ':0.57721566490153286060 , 'GAMMA':0.57721566490153286060,
	'DEG':57.29577951308232087680,
	'φ':1.6180339887498948482, 'PHI':1.6180339887498948482,
	'True':True , 'False':False  # Valores lógicos
}

""" Diccionario de funciones matemáticas y la referencia a la función """
funciones = {
	'sin':math.sin, 'cos':math.cos, 'tan':math.tan,
	'log':Log, 'log10':Log10,
	'exp':Exp,
	'sqrt':Sqrt,
	'abs':math.fabs,
	'int':int
}

variables = {}  # Diccionario que almacena el nombre(key) y valor(value) de las variables



tipoInstruccion = {
		'STOP':False,
		'constpush':programa.constpush,
		'varpush':programa.varpush,
		'evaluacion':programa.evaluacion,
		'suma':programa.suma,
		'resta':programa.resta,
		'multiplicacion':programa.multiplicacion,
		'division':programa.division,
		'modulo':programa.modulo,
		'negacion':programa.negacion,
		'potencia':programa.potencia,
		'asignacion':programa.asignacion,
		'funcion':programa.funcion,
		'print':programa.print,
		'mayorque':programa.mayorque,
		'menorque':programa.menorque,
		'igual':programa.igual,
		'mayorigual':programa.mayorigual,
		'menorigual':programa.menorigual,
		'diferente':programa.diferente,
		'and':programa.andcode,
		'or':programa.orcode,
		'not':programa.notcode,
		'if':programa.ifcode,
		'while':programa.whilecode,
		'for':programa.forcode
	}


"""
	MENSAJES CONSOLA
	>>>>>>>>>>>>>>>>
"""

def imprimirError(tipo,mensaje):
	print('\x1b[0;m'+'\x1b[3;31m'+'{} : {}'.format(tipo,mensaje)+'\x1b[0;m')

def imprimirNotificacion(mensaje):
	print('\x1b[1;33m'+'\n--- %s ---\n',mensaje)

def imprimirResultado(resultado):
	print('HOC4 >> ',resultado)
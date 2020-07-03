# -*- coding: utf-8 -*-
#@author: Lalo Valle

# Importacion del módulo de la implementación de lex en python
import ply.lex as lex
import Recursos as recursos

class AnalizadorLexico(object):

	tokens = recursos.tokens  # Lista de nombres de los tokens
	literals = recursos.literals

	""" 
		EXPRESIONES REGULARES DE LOS TOKENS 
		>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	"""

	t_ignore = ' \t\n' # Ignora espacios, tabuladores y saltos de línea

	t_INCREMENTO = r'\+\+'
	t_DECREMENTO = r'--'

	""" Operadores lógicos """
	t_OR = r'\|\|'
	t_AND = r'&&'
	t_MAYORIGUAL = r'>='
	t_MENORIGUAL = r'<='
	t_IGUALREL = r'=='
	t_DIFERENTE = r'!='

	t_CADENA = r'\'[\w ]*\''

	def t_NUMERO(self,t):
		r'\d+(\.\d+)?'
		if t.value.find('.') == -1 : t.value = int(t.value)
		else: t.value = float(t.value)
		return t

	def t_VARIABLE(self,t):
		r'[_a-zA-Z_][\w]*'
		valor = t.value

		if valor == 'print': t.type = 'PRINT'
		elif valor == 'if': t.type = 'IF'
		elif valor == 'else': t.type = 'ELSE'
		elif valor == 'while': t.type = 'WHILE'
		elif valor == 'for': t.type = 'FOR'
		elif valor in recursos.funciones: # Identificación de funciones
			t.type = 'FUNCION'
			t.value = recursos.funciones[t.value]
		elif valor in recursos.constantes: # Identificación de constantes
			t.type = 'CONSTANTE'
			t.value = recursos.constantes[t.value]
		else: # Identificación de variables(definidas e indefinidas)
			if t.value in recursos.variables: t.type = 'VARIABLE'
			else: t.type = 'INDEFINIDA'
		return t


	# Dado que las constantes tiene caracteres como letras griegas no basta con identificacion de alfanuméricos
	def t_CONSTANTE(self,t):
		r'[πΓφ]'
		t.type = 'CONSTANTE'
		t.value = recursos.constantes[t.value]
		if recursos._lex:
			recursos.agregarTokenTabla(t)
		return t

	def t_error(self,t):
		recursos.imprimirError('ErrorLexico','No se ha reconocido el caracter {} en la línea {}, posición {}'.format(t.value[0],t.lineno,t.lexpos))
		t.lexer.skip(1) 	# Salta la ejecución al lexema siguiente


	"""	
		MÉTODOS
		>>>>>>>
	"""
	def __init__(self):
		self.lexico = None

	def construir(self, **kwargs):
		self.lexico = lex.lex(object=self,**kwargs)

	def analizarCadena(self,cadena):
		tokens = []

		self.lexico.input(cadena)

		while True:
			tok = self.lexico.token()
			if not tok: break
			estado = '\nLexema: {}( {} )'.format(str(tok.value),str(tok.type))
			tokens.append(estado)

		return tokens
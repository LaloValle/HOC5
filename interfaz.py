import PySimpleGUI as sg

from AnalizadorLexico import *
import AnalizadorSintactico as sintactico
import Recursos as recursos
from Programa import Programa

sg.theme('GreenTan')  # No gray windows please!
btnLexico = 'Analizar léxicamente'
btnEjecuta = 'Ejecuta el programa escrito'
btnSintactico = 'Analizar sintácticamente'
txtInput= 'Caja de texto entrada'
txtOutput= 'Caja de texto salida del programa'
txtLex = 'Caja de texto Lex'
txtSin = 'Caja de texto Sintac'

""" Analizador léxico y sintáctico """
lexico = AnalizadorLexico()
lexico.construir()
sintactico.construir()

paso = 0

# STEP 1 define the layout
layout = [
		[sg.Text('Cadena a analizar léxicamente')],
		[
		sg.Multiline(key=txtInput, default_text='', size=(50, 10), pad=(0,0)),#entrada
		sg.Multiline(key=txtOutput, default_text='', size=(30, 10), pad=(0,0)),#salida
		],
		[
		sg.Multiline(key=txtLex, default_text='', size=(35, 20)),#análisis lex
        sg.Multiline(key=txtSin, default_text='', size=(50, 20)) #análisis sin
        ],
		[sg.Button(btnLexico), sg.Button(btnSintactico), sg.Button(btnEjecuta)]
        ]

#STEP 2 - create the window
window = sg.Window('HOC 5', layout, grab_anywhere=True)

""" Impresión de resultados llamados desde una función print"""
imprimir = False  # Activo cuando se tenga un nueva cadena a imprimir

# STEP3 - the event loop
while True:

	event, values = window.read()   # Read the event that happened and the values dictionary
	if event == sg.WIN_CLOSED:     # If user closed window with X or if user clicked "Exit" button then exit
		break
	if event == btnLexico:
		window[txtLex]('')
		tokens = lexico.analizarCadena(window[txtInput].get())
		for token in tokens:
			window[txtLex].Update(value=token, append=True)
		paso = 1

	elif event == btnSintactico and paso == 1:
		window[txtSin]('')
		try:
			s = window[txtInput].get()
		except EOFError:
			continue
		if not s:
			continue
		else:
			Programa.programa().reiniciarPrograma()
			for e in sintactico.analizarCadena(s):
				window[txtSin].Update(value=str(e) + '\n', append=True)
			
			paso = 2

	elif event == btnEjecuta and paso == 2:
		Programa.programa().ejecutar()
		window[txtOutput]('')
		for output in Programa.programa()._output:
				window[txtOutput].Update(value=output + '\n', append=True)		


window.close()

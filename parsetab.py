
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORleftANDleft>MAYORIGUAL<MENORIGUALIGUALRELDIFERENTEleft+-left*/%leftMENOSUNARIO!right^AND CADENA CONSTANTE DIFERENTE ELSE FOR FUNCION IF IGUALREL INDEFINIDA MAYORIGUAL MENORIGUAL NUMERO OR PRINT VARIABLE WHILE\n\tlista \t:\n\t\t\t| lista ';'\n\t\t\t| lista sentencia\n\t lista : lista error ';' \t\n\tasignacion  : VARIABLE '=' expresion\n\t\t\t\t| INDEFINIDA '=' expresion\n\t sentencia \t: asignacion ';'\n\t\t\t\t\t| '{' listasentencias '}'\n\t sentencia : PRINT '(' expresion ')' ';' \tsentencia : while condicion sentencia termino sentencia \t: if condicion sentencia termino\n\t\t\t\t\t| if condicion sentencia termino ELSE sentencia termino\n\t sentencia : for asignacion condicion sentencia termino  condicion : '(' expresion ')'  while : WHILE  if : IF  for : FOR  listasentencias :\n\t\t\t\t\t\t| listasentencias\n\t\t\t\t\t\t| listasentencias sentencia\n\t \n\texpresion \t: NUMERO \n\t\t\t\t| CONSTANTE\n\t\t\t\t| CADENA\n\t expresion : VARIABLE  expresion : asignacion  expresion \t: '!' expresion\n\t\t\t\t\t| '-' expresion %prec MENOSUNARIO\n\t expresion \t: FUNCION '(' expresion ')'\n\t\t\t\t\t| expresion '+' expresion\n\t\t\t\t\t| expresion '-' expresion\n\t\t\t\t\t| expresion '*' expresion\n\t\t\t\t\t| expresion '/' expresion\n\t\t\t\t\t| expresion '%' expresion\n\t\t\t\t\t| expresion '^' expresion\n\t\t\t\t\t| expresion '>' expresion\n\t\t\t\t\t| expresion MAYORIGUAL expresion\n\t\t\t\t\t| expresion '<' expresion\n\t\t\t\t\t| expresion MENORIGUAL expresion\n\t\t\t\t\t| expresion IGUALREL expresion\n\t\t\t\t\t| expresion DIFERENTE expresion\n\t\t\t\t\t| expresion AND expresion\n\t\t\t\t\t| expresion OR expresion\n\t termino :"
    
_lr_action_items = {';':([0,1,2,3,4,5,16,17,26,29,30,31,32,33,37,39,41,42,43,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,83,84,85,],[-1,2,-2,-3,16,17,-4,-7,-8,-21,-22,-23,-24,-25,-43,-43,-5,-6,65,-26,-27,-10,-11,-43,-9,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-13,-28,-43,-12,]),'error':([0,1,2,3,16,17,26,37,39,61,63,64,65,82,84,85,],[-1,4,-2,-3,-4,-7,-8,-43,-43,-10,-11,-43,-9,-13,-43,-12,]),'{':([0,1,2,3,6,16,17,18,20,22,26,27,37,39,40,61,62,63,64,65,81,82,84,85,],[-1,6,-2,-3,-18,-4,-7,6,6,6,-8,-20,-43,-43,6,-10,-14,-11,-43,-9,6,-13,-43,-12,]),'PRINT':([0,1,2,3,6,16,17,18,20,22,26,27,37,39,40,61,62,63,64,65,81,82,84,85,],[-1,7,-2,-3,-18,-4,-7,7,7,7,-8,-20,-43,-43,7,-10,-14,-11,-43,-9,7,-13,-43,-12,]),'VARIABLE':([0,1,2,3,6,10,15,16,17,18,19,20,21,22,24,25,26,27,34,35,37,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,61,62,63,64,65,81,82,84,85,],[-1,11,-2,-3,-18,11,-17,-4,-7,11,32,11,32,11,32,32,-8,-20,32,32,-43,-43,11,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-10,-14,-11,-43,-9,11,-13,-43,-12,]),'INDEFINIDA':([0,1,2,3,6,10,15,16,17,18,19,20,21,22,24,25,26,27,34,35,37,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,61,62,63,64,65,81,82,84,85,],[-1,12,-2,-3,-18,12,-17,-4,-7,12,12,12,12,12,12,12,-8,-20,12,12,-43,-43,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-10,-14,-11,-43,-9,12,-13,-43,-12,]),'WHILE':([0,1,2,3,6,16,17,18,20,22,26,27,37,39,40,61,62,63,64,65,81,82,84,85,],[-1,13,-2,-3,-18,-4,-7,13,13,13,-8,-20,-43,-43,13,-10,-14,-11,-43,-9,13,-13,-43,-12,]),'IF':([0,1,2,3,6,16,17,18,20,22,26,27,37,39,40,61,62,63,64,65,81,82,84,85,],[-1,14,-2,-3,-18,-4,-7,14,14,14,-8,-20,-43,-43,14,-10,-14,-11,-43,-9,14,-13,-43,-12,]),'FOR':([0,1,2,3,6,16,17,18,20,22,26,27,37,39,40,61,62,63,64,65,81,82,84,85,],[-1,15,-2,-3,-18,-4,-7,15,15,15,-8,-20,-43,-43,15,-10,-14,-11,-43,-9,15,-13,-43,-12,]),'$end':([0,1,2,3,16,17,26,37,39,61,63,64,65,82,84,85,],[-1,0,-2,-3,-4,-7,-8,-43,-43,-10,-11,-43,-9,-13,-43,-12,]),'}':([6,17,18,26,27,37,39,61,63,64,65,82,84,85,],[-18,-7,26,-8,-20,-43,-43,-10,-11,-43,-9,-13,-43,-12,]),'(':([7,8,9,13,14,23,29,30,31,32,33,36,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,],[19,21,21,-15,-16,21,-21,-22,-23,-24,-25,60,-5,-6,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-28,]),'=':([11,12,32,],[24,25,24,]),'ELSE':([17,26,37,39,61,63,64,65,82,84,85,],[-7,-8,-43,-43,-10,81,-43,-9,-13,-43,-12,]),'NUMERO':([19,21,24,25,34,35,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'CONSTANTE':([19,21,24,25,34,35,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'CADENA':([19,21,24,25,34,35,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'!':([19,21,24,25,34,35,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'-':([19,21,24,25,28,29,30,31,32,33,34,35,38,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[35,35,35,35,45,-21,-22,-23,-24,-25,35,35,45,45,45,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-26,-27,35,-29,-30,-31,-32,-33,-34,45,45,45,45,45,45,45,45,45,-28,]),'FUNCION':([19,21,24,25,34,35,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),')':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[43,-21,-22,-23,-24,-25,62,-5,-6,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,83,-28,]),'+':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[44,-21,-22,-23,-24,-25,44,44,44,-26,-27,-29,-30,-31,-32,-33,-34,44,44,44,44,44,44,44,44,44,-28,]),'*':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[46,-21,-22,-23,-24,-25,46,46,46,-26,-27,46,46,-31,-32,-33,-34,46,46,46,46,46,46,46,46,46,-28,]),'/':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[47,-21,-22,-23,-24,-25,47,47,47,-26,-27,47,47,-31,-32,-33,-34,47,47,47,47,47,47,47,47,47,-28,]),'%':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[48,-21,-22,-23,-24,-25,48,48,48,-26,-27,48,48,-31,-32,-33,-34,48,48,48,48,48,48,48,48,48,-28,]),'^':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[49,-21,-22,-23,-24,-25,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-28,]),'>':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[50,-21,-22,-23,-24,-25,50,50,50,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,50,50,50,-28,]),'MAYORIGUAL':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[51,-21,-22,-23,-24,-25,51,51,51,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,51,51,51,-28,]),'<':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[52,-21,-22,-23,-24,-25,52,52,52,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,52,52,52,-28,]),'MENORIGUAL':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[53,-21,-22,-23,-24,-25,53,53,53,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,53,53,53,-28,]),'IGUALREL':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[54,-21,-22,-23,-24,-25,54,54,54,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,54,54,54,-28,]),'DIFERENTE':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[55,-21,-22,-23,-24,-25,55,55,55,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,55,55,55,-28,]),'AND':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[56,-21,-22,-23,-24,-25,56,56,56,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,56,56,-28,]),'OR':([28,29,30,31,32,33,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,83,],[57,-21,-22,-23,-24,-25,57,57,57,-26,-27,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,57,-28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista':([0,],[1,]),'sentencia':([1,18,20,22,40,81,],[3,27,37,39,64,84,]),'asignacion':([1,10,18,19,20,21,22,24,25,34,35,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,81,],[5,23,5,33,5,33,5,33,33,33,33,5,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,5,]),'while':([1,18,20,22,40,81,],[8,8,8,8,8,8,]),'if':([1,18,20,22,40,81,],[9,9,9,9,9,9,]),'for':([1,18,20,22,40,81,],[10,10,10,10,10,10,]),'listasentencias':([6,],[18,]),'condicion':([8,9,23,],[20,22,40,]),'expresion':([19,21,24,25,34,35,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,],[28,38,41,42,58,59,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,]),'termino':([37,39,64,84,],[61,63,82,85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lista","S'",1,None,None,None),
  ('lista -> <empty>','lista',0,'p_lista','AnalizadorSintactico.py',30),
  ('lista -> lista ;','lista',2,'p_lista','AnalizadorSintactico.py',31),
  ('lista -> lista sentencia','lista',2,'p_lista','AnalizadorSintactico.py',32),
  ('lista -> lista error ;','lista',3,'p_lista_error','AnalizadorSintactico.py',40),
  ('asignacion -> VARIABLE = expresion','asignacion',3,'p_asignacion','AnalizadorSintactico.py',48),
  ('asignacion -> INDEFINIDA = expresion','asignacion',3,'p_asignacion','AnalizadorSintactico.py',49),
  ('sentencia -> asignacion ;','sentencia',2,'p_sentencia','AnalizadorSintactico.py',56),
  ('sentencia -> { listasentencias }','sentencia',3,'p_sentencia','AnalizadorSintactico.py',57),
  ('sentencia -> PRINT ( expresion ) ;','sentencia',5,'p_sentencia_print','AnalizadorSintactico.py',65),
  ('sentencia -> while condicion sentencia termino','sentencia',4,'p_sentencia_while','AnalizadorSintactico.py',70),
  ('sentencia -> if condicion sentencia termino','sentencia',4,'p_sentencia_if','AnalizadorSintactico.py',77),
  ('sentencia -> if condicion sentencia termino ELSE sentencia termino','sentencia',7,'p_sentencia_if','AnalizadorSintactico.py',78),
  ('sentencia -> for asignacion condicion sentencia termino','sentencia',5,'p_sentencia_for','AnalizadorSintactico.py',89),
  ('condicion -> ( expresion )','condicion',3,'p_condicion','AnalizadorSintactico.py',97),
  ('while -> WHILE','while',1,'p_while','AnalizadorSintactico.py',102),
  ('if -> IF','if',1,'p_if','AnalizadorSintactico.py',107),
  ('for -> FOR','for',1,'p_for','AnalizadorSintactico.py',112),
  ('listasentencias -> <empty>','listasentencias',0,'p_listasentencias','AnalizadorSintactico.py',117),
  ('listasentencias -> listasentencias','listasentencias',1,'p_listasentencias','AnalizadorSintactico.py',118),
  ('listasentencias -> listasentencias sentencia','listasentencias',2,'p_listasentencias','AnalizadorSintactico.py',119),
  ('expresion -> NUMERO','expresion',1,'p_expresion_constantes','AnalizadorSintactico.py',129),
  ('expresion -> CONSTANTE','expresion',1,'p_expresion_constantes','AnalizadorSintactico.py',130),
  ('expresion -> CADENA','expresion',1,'p_expresion_constantes','AnalizadorSintactico.py',131),
  ('expresion -> VARIABLE','expresion',1,'p_expresion_variable','AnalizadorSintactico.py',136),
  ('expresion -> asignacion','expresion',1,'p_expresion_asignacion','AnalizadorSintactico.py',140),
  ('expresion -> ! expresion','expresion',2,'p_expresion_negaciones','AnalizadorSintactico.py',144),
  ('expresion -> - expresion','expresion',2,'p_expresion_negaciones','AnalizadorSintactico.py',145),
  ('expresion -> FUNCION ( expresion )','expresion',4,'p_expresion_operaciones','AnalizadorSintactico.py',152),
  ('expresion -> expresion + expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',153),
  ('expresion -> expresion - expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',154),
  ('expresion -> expresion * expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',155),
  ('expresion -> expresion / expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',156),
  ('expresion -> expresion % expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',157),
  ('expresion -> expresion ^ expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',158),
  ('expresion -> expresion > expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',159),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',160),
  ('expresion -> expresion < expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',161),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',162),
  ('expresion -> expresion IGUALREL expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',163),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',164),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',165),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',166),
  ('termino -> <empty>','termino',0,'p_termino','AnalizadorSintactico.py',190),
]

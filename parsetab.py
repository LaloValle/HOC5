
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORleftANDleft>MAYORIGUAL<MENORIGUALIGUALRELDIFERENTEleft+-left*/%leftMENOSUNARIO!right^AND CONSTANTE DIFERENTE ELSE FOR FUNCION IF IGUALREL INDEFINIDA MAYORIGUAL MENORIGUAL NUMERO OR PRINT VARIABLE WHILE\n\tlista \t:\n\t\t\t| lista ';'\n\t\t\t| lista sentencia\n\t lista : lista error ';' \t\n\tasignacion  : VARIABLE '=' expresion\n\t\t\t\t| INDEFINIDA '=' expresion\n\t sentencia \t: asignacion ';'\n\t\t\t\t\t| '{' listasentencias '}'\n\t sentencia : PRINT '(' expresion ')' ';' \tsentencia : while condicion sentencia termino sentencia \t: if condicion sentencia termino\n\t\t\t\t\t| if condicion sentencia termino ELSE sentencia termino\n\t sentencia : for asignacion condicion sentencia termino  condicion : '(' expresion ')'  while : WHILE  if : IF  for : FOR  listasentencias :\n\t\t\t\t\t\t| listasentencias\n\t\t\t\t\t\t| listasentencias sentencia\n\t \n\texpresion \t: NUMERO \n\t\t\t\t| CONSTANTE\t\n\t expresion : VARIABLE  expresion : asignacion  expresion \t: '!' expresion\n\t\t\t\t\t| '-' expresion %prec MENOSUNARIO\n\t expresion \t: FUNCION '(' expresion ')'\n\t\t\t\t\t| expresion '+' expresion\n\t\t\t\t\t| expresion '-' expresion\n\t\t\t\t\t| expresion '*' expresion\n\t\t\t\t\t| expresion '/' expresion\n\t\t\t\t\t| expresion '%' expresion\n\t\t\t\t\t| expresion '^' expresion\n\t\t\t\t\t| expresion '>' expresion\n\t\t\t\t\t| expresion MAYORIGUAL expresion\n\t\t\t\t\t| expresion '<' expresion\n\t\t\t\t\t| expresion MENORIGUAL expresion\n\t\t\t\t\t| expresion IGUALREL expresion\n\t\t\t\t\t| expresion DIFERENTE expresion\n\t\t\t\t\t| expresion AND expresion\n\t\t\t\t\t| expresion OR expresion\n\t termino :"
    
_lr_action_items = {';':([0,1,2,3,4,5,16,17,26,29,30,31,32,36,38,40,41,42,57,58,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,82,83,84,],[-1,2,-2,-3,16,17,-4,-7,-8,-21,-22,-23,-24,-42,-42,-5,-6,64,-25,-26,-10,-11,-42,-9,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-27,-42,-12,]),'error':([0,1,2,3,16,17,26,36,38,60,62,63,64,81,83,84,],[-1,4,-2,-3,-4,-7,-8,-42,-42,-10,-11,-42,-9,-13,-42,-12,]),'{':([0,1,2,3,6,16,17,18,20,22,26,27,36,38,39,60,61,62,63,64,80,81,83,84,],[-1,6,-2,-3,-18,-4,-7,6,6,6,-8,-20,-42,-42,6,-10,-14,-11,-42,-9,6,-13,-42,-12,]),'PRINT':([0,1,2,3,6,16,17,18,20,22,26,27,36,38,39,60,61,62,63,64,80,81,83,84,],[-1,7,-2,-3,-18,-4,-7,7,7,7,-8,-20,-42,-42,7,-10,-14,-11,-42,-9,7,-13,-42,-12,]),'VARIABLE':([0,1,2,3,6,10,15,16,17,18,19,20,21,22,24,25,26,27,33,34,36,38,39,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,60,61,62,63,64,80,81,83,84,],[-1,11,-2,-3,-18,11,-17,-4,-7,11,31,11,31,11,31,31,-8,-20,31,31,-42,-42,11,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-10,-14,-11,-42,-9,11,-13,-42,-12,]),'INDEFINIDA':([0,1,2,3,6,10,15,16,17,18,19,20,21,22,24,25,26,27,33,34,36,38,39,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,60,61,62,63,64,80,81,83,84,],[-1,12,-2,-3,-18,12,-17,-4,-7,12,12,12,12,12,12,12,-8,-20,12,12,-42,-42,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-10,-14,-11,-42,-9,12,-13,-42,-12,]),'WHILE':([0,1,2,3,6,16,17,18,20,22,26,27,36,38,39,60,61,62,63,64,80,81,83,84,],[-1,13,-2,-3,-18,-4,-7,13,13,13,-8,-20,-42,-42,13,-10,-14,-11,-42,-9,13,-13,-42,-12,]),'IF':([0,1,2,3,6,16,17,18,20,22,26,27,36,38,39,60,61,62,63,64,80,81,83,84,],[-1,14,-2,-3,-18,-4,-7,14,14,14,-8,-20,-42,-42,14,-10,-14,-11,-42,-9,14,-13,-42,-12,]),'FOR':([0,1,2,3,6,16,17,18,20,22,26,27,36,38,39,60,61,62,63,64,80,81,83,84,],[-1,15,-2,-3,-18,-4,-7,15,15,15,-8,-20,-42,-42,15,-10,-14,-11,-42,-9,15,-13,-42,-12,]),'$end':([0,1,2,3,16,17,26,36,38,60,62,63,64,81,83,84,],[-1,0,-2,-3,-4,-7,-8,-42,-42,-10,-11,-42,-9,-13,-42,-12,]),'}':([6,17,18,26,27,36,38,60,62,63,64,81,83,84,],[-18,-7,26,-8,-20,-42,-42,-10,-11,-42,-9,-13,-42,-12,]),'(':([7,8,9,13,14,23,29,30,31,32,35,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,82,],[19,21,21,-15,-16,21,-21,-22,-23,-24,59,-5,-6,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-27,]),'=':([11,12,31,],[24,25,24,]),'ELSE':([17,26,36,38,60,62,63,64,81,83,84,],[-7,-8,-42,-42,-10,80,-42,-9,-13,-42,-12,]),'NUMERO':([19,21,24,25,33,34,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'CONSTANTE':([19,21,24,25,33,34,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'!':([19,21,24,25,33,34,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'-':([19,21,24,25,28,29,30,31,32,33,34,37,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[34,34,34,34,44,-21,-22,-23,-24,34,34,44,44,44,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-25,-26,34,-28,-29,-30,-31,-32,-33,44,44,44,44,44,44,44,44,44,-27,]),'FUNCION':([19,21,24,25,33,34,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),')':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[42,-21,-22,-23,-24,61,-5,-6,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,82,-27,]),'+':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[43,-21,-22,-23,-24,43,43,43,-25,-26,-28,-29,-30,-31,-32,-33,43,43,43,43,43,43,43,43,43,-27,]),'*':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[45,-21,-22,-23,-24,45,45,45,-25,-26,45,45,-30,-31,-32,-33,45,45,45,45,45,45,45,45,45,-27,]),'/':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[46,-21,-22,-23,-24,46,46,46,-25,-26,46,46,-30,-31,-32,-33,46,46,46,46,46,46,46,46,46,-27,]),'%':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[47,-21,-22,-23,-24,47,47,47,-25,-26,47,47,-30,-31,-32,-33,47,47,47,47,47,47,47,47,47,-27,]),'^':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[48,-21,-22,-23,-24,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-27,]),'>':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[49,-21,-22,-23,-24,49,49,49,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,49,49,49,-27,]),'MAYORIGUAL':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[50,-21,-22,-23,-24,50,50,50,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,50,50,50,-27,]),'<':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[51,-21,-22,-23,-24,51,51,51,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,51,51,51,-27,]),'MENORIGUAL':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[52,-21,-22,-23,-24,52,52,52,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,52,52,52,-27,]),'IGUALREL':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[53,-21,-22,-23,-24,53,53,53,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,53,53,53,-27,]),'DIFERENTE':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[54,-21,-22,-23,-24,54,54,54,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,54,54,54,-27,]),'AND':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[55,-21,-22,-23,-24,55,55,55,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,55,55,-27,]),'OR':([28,29,30,31,32,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,],[56,-21,-22,-23,-24,56,56,56,-25,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,56,-27,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista':([0,],[1,]),'sentencia':([1,18,20,22,39,80,],[3,27,36,38,63,83,]),'asignacion':([1,10,18,19,20,21,22,24,25,33,34,39,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,80,],[5,23,5,32,5,32,5,32,32,32,32,5,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,5,]),'while':([1,18,20,22,39,80,],[8,8,8,8,8,8,]),'if':([1,18,20,22,39,80,],[9,9,9,9,9,9,]),'for':([1,18,20,22,39,80,],[10,10,10,10,10,10,]),'listasentencias':([6,],[18,]),'condicion':([8,9,23,],[20,22,39,]),'expresion':([19,21,24,25,33,34,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,],[28,37,40,41,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,]),'termino':([36,38,63,83,],[60,62,81,84,]),}

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
  ('lista -> lista error ;','lista',3,'p_lista_error','AnalizadorSintactico.py',41),
  ('asignacion -> VARIABLE = expresion','asignacion',3,'p_asignacion','AnalizadorSintactico.py',49),
  ('asignacion -> INDEFINIDA = expresion','asignacion',3,'p_asignacion','AnalizadorSintactico.py',50),
  ('sentencia -> asignacion ;','sentencia',2,'p_sentencia','AnalizadorSintactico.py',58),
  ('sentencia -> { listasentencias }','sentencia',3,'p_sentencia','AnalizadorSintactico.py',59),
  ('sentencia -> PRINT ( expresion ) ;','sentencia',5,'p_sentencia_print','AnalizadorSintactico.py',68),
  ('sentencia -> while condicion sentencia termino','sentencia',4,'p_sentencia_while','AnalizadorSintactico.py',74),
  ('sentencia -> if condicion sentencia termino','sentencia',4,'p_sentencia_if','AnalizadorSintactico.py',81),
  ('sentencia -> if condicion sentencia termino ELSE sentencia termino','sentencia',7,'p_sentencia_if','AnalizadorSintactico.py',82),
  ('sentencia -> for asignacion condicion sentencia termino','sentencia',5,'p_sentencia_for','AnalizadorSintactico.py',93),
  ('condicion -> ( expresion )','condicion',3,'p_condicion','AnalizadorSintactico.py',101),
  ('while -> WHILE','while',1,'p_while','AnalizadorSintactico.py',107),
  ('if -> IF','if',1,'p_if','AnalizadorSintactico.py',113),
  ('for -> FOR','for',1,'p_for','AnalizadorSintactico.py',119),
  ('listasentencias -> <empty>','listasentencias',0,'p_listasentencias','AnalizadorSintactico.py',125),
  ('listasentencias -> listasentencias','listasentencias',1,'p_listasentencias','AnalizadorSintactico.py',126),
  ('listasentencias -> listasentencias sentencia','listasentencias',2,'p_listasentencias','AnalizadorSintactico.py',127),
  ('expresion -> NUMERO','expresion',1,'p_expresion_constantes','AnalizadorSintactico.py',137),
  ('expresion -> CONSTANTE','expresion',1,'p_expresion_constantes','AnalizadorSintactico.py',138),
  ('expresion -> VARIABLE','expresion',1,'p_expresion_variable','AnalizadorSintactico.py',144),
  ('expresion -> asignacion','expresion',1,'p_expresion_asignacion','AnalizadorSintactico.py',149),
  ('expresion -> ! expresion','expresion',2,'p_expresion_negaciones','AnalizadorSintactico.py',154),
  ('expresion -> - expresion','expresion',2,'p_expresion_negaciones','AnalizadorSintactico.py',155),
  ('expresion -> FUNCION ( expresion )','expresion',4,'p_expresion_operaciones','AnalizadorSintactico.py',163),
  ('expresion -> expresion + expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',164),
  ('expresion -> expresion - expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',165),
  ('expresion -> expresion * expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',166),
  ('expresion -> expresion / expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',167),
  ('expresion -> expresion % expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',168),
  ('expresion -> expresion ^ expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',169),
  ('expresion -> expresion > expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',170),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',171),
  ('expresion -> expresion < expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',172),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',173),
  ('expresion -> expresion IGUALREL expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',174),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',175),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',176),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_operaciones','AnalizadorSintactico.py',177),
  ('termino -> <empty>','termino',0,'p_termino','AnalizadorSintactico.py',202),
]
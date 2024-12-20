
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIVIDE ID LPAREN MINUS NUMBER PLUS RPAREN TIMESexpression : expression PLUS termexpression : termterm : NUMBER'
    
_lr_action_items = {'NUMBER':([0,4,],[3,3,]),'$end':([1,2,3,5,],[0,-2,-3,-1,]),'PLUS':([1,2,3,5,],[4,-2,-3,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[1,]),'term':([0,4,],[2,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parser.py',6),
  ('expression -> term','expression',1,'p_expression_term','parser.py',10),
  ('term -> NUMBER','term',1,'p_term_number','parser.py',14),
]

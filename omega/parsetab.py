
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'Begin_Subroutines_Declaration Begin_Variables_Declaration End_Subroutines_Declaration End_Variables_Declaration call cin close_brace close_parenthesis comma cout do double double_number else elseif equal for greater_or_equal greater_than identifier if in int int_number is_equal less_or_equal less_than minus minus_minus not_equal open_brace open_parenthesis out plus plus_plus semicolon slash star string while\n\t\tProgramFlow : VariablesDeclaration SubroutinesDeclaration\n\t\n\t\tAssignmentStatement : identifier equal ArithmeticExpression\n\t\n\t\tVariablesDeclaration : Begin_Variables_Declaration SingleTypeVariableDeclaration End_Variables_Declaration\n\t\n\t\tSingleTypeVariableDeclaration : SimpleTypes SequenceOfIdentifiers semicolon SingleTypeVariableDeclaration\n\t\t\t\t\t\t\t\t\t  |\n\t\n\t\tSimpleTypes : int\n\t\t\t\t\t| double \n\t\n\t\tSequenceOfIdentifiers \t:\tidentifier \n\t\t\t\t\t\t\t\t\t|\tidentifier comma SequenceOfIdentifiers\n\t\t\t\t\t\t\t\t\t|\tAssignmentStatement\n\t\t\t\t\t\t\t\t\t|\tAssignmentStatement comma SequenceOfIdentifiers\n\t\n\t\tArithmeticExpression : Number\n\t\t\t\t   | UnaryOperation\n\t\t\t\t   | open_parenthesis ArithmeticExpression close_parenthesis\n\t\t\t\t   | open_parenthesis ArithmeticExpression close_parenthesis plus ArithmeticExpression\n\t\t\t\t   | open_parenthesis ArithmeticExpression close_parenthesis minus ArithmeticExpression\n\t\t\t\t   | open_parenthesis ArithmeticExpression close_parenthesis star ArithmeticExpression\n\t\t\t\t   | open_parenthesis ArithmeticExpression close_parenthesis slash ArithmeticExpression\n\t\t\t\t   | Number plus ArithmeticExpression\n\t\t\t\t   | Number minus ArithmeticExpression\n\t\t\t\t   | Number star ArithmeticExpression\n\t\t\t\t   | Number slash ArithmeticExpression\n\t\t\t\t   | UnaryOperation plus ArithmeticExpression\n\t\t\t\t   | UnaryOperation minus ArithmeticExpression\n\t\t\t\t   | UnaryOperation star ArithmeticExpression\n\t\t\t\t   | UnaryOperation slash ArithmeticExpression\n\t\n\t\tUnaryOperation : plus_plus identifier\n\t\t\t\t\t   | minus_minus identifier\n\t\t\t\t\t   | identifier plus_plus\n\t\t\t\t\t   | identifier minus_minus\n\t\n\t\tNumber : int_number\n\t\t\t   | double_number\n\t\t\t   | identifier\n\t\n\t\tBooleanExpression : ArithmeticExpression LogicOperator ArithmeticExpression\n\t\n\t\tLogicOperator : is_equal\n\t\t\t\t\t  |\tnot_equal\n\t\t\t\t\t  |\tless_or_equal\n\t\t\t\t\t  |\tgreater_or_equal\n\t\t\t\t\t  |\tless_than\n\t\t\t\t\t  |\tgreater_than\n\t\n\t\tifCondition : if open_parenthesis BooleanExpression close_parenthesis open_brace Routine close_brace elseIfCondition\n\t\n\t\telseIfCondition : elseif open_parenthesis BooleanExpression close_parenthesis open_brace Routine close_brace elseIfCondition\n\t\t\t\t\t\t| elseCondition\n\t\n\t\telseCondition : else open_brace Routine close_brace\n\t\t\t\t\t  |\n\t\n\t\twhileLoop : while open_parenthesis BooleanExpression close_parenthesis open_brace Routine close_brace\n\t\n\t\tdoWhileLoop : do open_brace Routine close_brace while open_parenthesis BooleanExpression close_parenthesis semicolon\n\t\n\t\tforLoop : for open_parenthesis SequenceOfIdentifiers semicolon BooleanExpression semicolon UpdateVariables close_parenthesis open_brace Routine close_brace\n\t\n\tUpdateVariables : AssignmentStatement\n\t\t\t\t\t| AssignmentStatement comma UpdateVariables\n\t\t\t\t\t| UnaryOperation\n\t\t\t\t\t| UnaryOperation comma UpdateVariables\n \t\n\t\tRoutine : AssignmentStatement semicolon Routine\n\t\t\t\t| UnaryOperation semicolon Routine\n\t\t\t\t| ifCondition Routine\n\t\t\t\t| whileLoop Routine\n\t\t\t\t| doWhileLoop Routine\n\t\t\t\t| forLoop Routine\n\t\t\t\t| call identifier Routine\n\t\t\t\t| InOut Routine\n\t\t\t\t|\n\t\n\t\tSubroutinesDeclaration : Begin_Subroutines_Declaration SingleSubroutine End_Subroutines_Declaration\n\t\n\t\tSingleSubroutine : identifier open_brace Routine close_brace SingleSubroutine\n\t\t\t\t\t\t |\n\t\n\t\tInOut : cin in identifier RecursiveIn semicolon\n\t\t\t  | cout out identifier RecursiveOut semicolon\n\t\n\t\tRecursiveIn : in identifier RecursiveIn\n\t\t\t\t\t|\n\t\n\t\tRecursiveOut : out identifier RecursiveOut\n\t\t\t\t\t|\n\t'
    
_lr_action_items = {'Begin_Variables_Declaration':([0,],[3,]),'$end':([1,4,16,],[0,-1,-62,]),'Begin_Subroutines_Declaration':([2,12,],[5,-3,]),'End_Variables_Declaration':([3,6,18,40,],[-5,12,-5,-4,]),'int':([3,18,],[8,8,]),'double':([3,18,],[9,9,]),'identifier':([5,7,8,9,17,19,20,21,26,27,28,29,30,31,32,33,46,52,53,54,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,99,100,101,102,103,104,105,108,109,111,113,114,115,116,117,119,123,125,132,133,136,137,142,144,148,149,150,151,152,153,160,161,162,164,165,],[11,14,-6,-7,22,14,42,14,22,22,22,22,59,22,61,62,42,11,22,22,22,42,42,22,14,87,88,42,42,42,42,42,42,42,42,42,-35,-36,-37,-38,-39,-40,42,122,124,42,42,42,42,22,22,-65,-66,42,22,-45,-46,-41,-43,22,22,42,22,-47,22,-44,-48,22,-45,-42,]),'End_Subroutines_Declaration':([5,10,52,78,],[-64,16,-64,-63,]),'open_brace':([11,36,98,106,145,147,159,],[17,65,117,119,151,153,162,]),'semicolon':([13,14,15,24,25,41,42,43,44,45,47,48,49,50,51,61,62,86,87,88,89,90,91,92,93,94,95,96,97,110,112,118,121,122,124,126,127,128,129,134,135,146,],[18,-8,-10,53,54,-9,-33,-2,-12,-13,-31,-32,-11,-29,-30,-27,-28,108,-68,-70,-19,-20,-21,-22,-23,-24,-25,-26,-14,123,125,-34,133,-68,-70,-15,-16,-17,-18,-67,-69,152,]),'comma':([14,15,42,43,44,45,47,48,50,51,61,62,89,90,91,92,93,94,95,96,97,126,127,128,129,140,141,],[19,21,-33,-2,-12,-13,-31,-32,-29,-30,-27,-28,-19,-20,-21,-22,-23,-24,-25,-26,-14,-15,-16,-17,-18,148,149,]),'equal':([14,22,],[20,20,]),'call':([17,26,27,28,29,31,53,54,59,65,117,119,123,125,136,137,142,144,151,152,153,160,161,162,164,165,],[30,30,30,30,30,30,30,30,30,30,30,30,-65,-66,-45,-46,-41,-43,30,-47,30,-44,-48,30,-45,-42,]),'close_brace':([17,23,26,27,28,29,31,53,54,55,56,57,58,59,60,65,79,80,81,85,117,119,123,125,130,131,136,137,142,144,151,152,153,157,158,160,161,162,163,164,165,],[-61,52,-61,-61,-61,-61,-61,-61,-61,-55,-56,-57,-58,-61,-60,-61,-53,-54,-59,107,-61,-61,-65,-66,136,137,-45,-46,-41,-43,-61,-47,-61,160,161,-44,-48,-61,164,-45,-42,]),'plus_plus':([17,20,22,26,27,28,29,31,42,46,53,54,59,63,64,65,69,70,71,72,73,74,75,76,99,100,101,102,103,104,105,108,113,114,115,116,117,119,123,125,132,133,136,137,142,144,148,149,150,151,152,153,160,161,162,164,165,],[32,32,50,32,32,32,32,32,50,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-35,-36,-37,-38,-39,-40,32,32,32,32,32,32,32,-65,-66,32,32,-45,-46,-41,-43,32,32,32,32,-47,32,-44,-48,32,-45,-42,]),'minus_minus':([17,20,22,26,27,28,29,31,42,46,53,54,59,63,64,65,69,70,71,72,73,74,75,76,99,100,101,102,103,104,105,108,113,114,115,116,117,119,123,125,132,133,136,137,142,144,148,149,150,151,152,153,160,161,162,164,165,],[33,33,51,33,33,33,33,33,51,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-35,-36,-37,-38,-39,-40,33,33,33,33,33,33,33,-65,-66,33,33,-45,-46,-41,-43,33,33,33,33,-47,33,-44,-48,33,-45,-42,]),'if':([17,26,27,28,29,31,53,54,59,65,117,119,123,125,136,137,142,144,151,152,153,160,161,162,164,165,],[34,34,34,34,34,34,34,34,34,34,34,34,-65,-66,-45,-46,-41,-43,34,-47,34,-44,-48,34,-45,-42,]),'while':([17,26,27,28,29,31,53,54,59,65,107,117,119,123,125,136,137,142,144,151,152,153,160,161,162,164,165,],[35,35,35,35,35,35,35,35,35,35,120,35,35,-65,-66,-45,-46,-41,-43,35,-47,35,-44,-48,35,-45,-42,]),'do':([17,26,27,28,29,31,53,54,59,65,117,119,123,125,136,137,142,144,151,152,153,160,161,162,164,165,],[36,36,36,36,36,36,36,36,36,36,36,36,-65,-66,-45,-46,-41,-43,36,-47,36,-44,-48,36,-45,-42,]),'for':([17,26,27,28,29,31,53,54,59,65,117,119,123,125,136,137,142,144,151,152,153,160,161,162,164,165,],[37,37,37,37,37,37,37,37,37,37,37,37,-65,-66,-45,-46,-41,-43,37,-47,37,-44,-48,37,-45,-42,]),'cin':([17,26,27,28,29,31,53,54,59,65,117,119,123,125,136,137,142,144,151,152,153,160,161,162,164,165,],[38,38,38,38,38,38,38,38,38,38,38,38,-65,-66,-45,-46,-41,-43,38,-47,38,-44,-48,38,-45,-42,]),'cout':([17,26,27,28,29,31,53,54,59,65,117,119,123,125,136,137,142,144,151,152,153,160,161,162,164,165,],[39,39,39,39,39,39,39,39,39,39,39,39,-65,-66,-45,-46,-41,-43,39,-47,39,-44,-48,39,-45,-42,]),'open_parenthesis':([20,34,35,37,46,63,64,69,70,71,72,73,74,75,76,99,100,101,102,103,104,105,108,113,114,115,116,120,132,143,150,],[46,63,64,66,46,46,46,46,46,46,46,46,46,46,46,46,-35,-36,-37,-38,-39,-40,46,46,46,46,46,132,46,150,46,]),'int_number':([20,46,63,64,69,70,71,72,73,74,75,76,99,100,101,102,103,104,105,108,113,114,115,116,132,150,],[47,47,47,47,47,47,47,47,47,47,47,47,47,-35,-36,-37,-38,-39,-40,47,47,47,47,47,47,47,]),'double_number':([20,46,63,64,69,70,71,72,73,74,75,76,99,100,101,102,103,104,105,108,113,114,115,116,132,150,],[48,48,48,48,48,48,48,48,48,48,48,48,48,-35,-36,-37,-38,-39,-40,48,48,48,48,48,48,48,]),'in':([38,87,122,],[67,109,109,]),'out':([39,88,124,],[68,111,111,]),'plus':([42,44,45,47,48,50,51,61,62,97,],[-33,69,73,-31,-32,-29,-30,-27,-28,113,]),'minus':([42,44,45,47,48,50,51,61,62,97,],[-33,70,74,-31,-32,-29,-30,-27,-28,114,]),'star':([42,44,45,47,48,50,51,61,62,97,],[-33,71,75,-31,-32,-29,-30,-27,-28,115,]),'slash':([42,44,45,47,48,50,51,61,62,97,],[-33,72,76,-31,-32,-29,-30,-27,-28,116,]),'close_parenthesis':([42,43,44,45,47,48,50,51,61,62,77,82,84,89,90,91,92,93,94,95,96,97,118,126,127,128,129,138,139,140,141,154,155,156,],[-33,-2,-12,-13,-31,-32,-29,-30,-27,-28,97,98,106,-19,-20,-21,-22,-23,-24,-25,-26,-14,-34,-15,-16,-17,-18,146,147,-49,-51,-50,-52,159,]),'is_equal':([42,44,45,47,48,50,51,61,62,83,89,90,91,92,93,94,95,96,97,126,127,128,129,],[-33,-12,-13,-31,-32,-29,-30,-27,-28,100,-19,-20,-21,-22,-23,-24,-25,-26,-14,-15,-16,-17,-18,]),'not_equal':([42,44,45,47,48,50,51,61,62,83,89,90,91,92,93,94,95,96,97,126,127,128,129,],[-33,-12,-13,-31,-32,-29,-30,-27,-28,101,-19,-20,-21,-22,-23,-24,-25,-26,-14,-15,-16,-17,-18,]),'less_or_equal':([42,44,45,47,48,50,51,61,62,83,89,90,91,92,93,94,95,96,97,126,127,128,129,],[-33,-12,-13,-31,-32,-29,-30,-27,-28,102,-19,-20,-21,-22,-23,-24,-25,-26,-14,-15,-16,-17,-18,]),'greater_or_equal':([42,44,45,47,48,50,51,61,62,83,89,90,91,92,93,94,95,96,97,126,127,128,129,],[-33,-12,-13,-31,-32,-29,-30,-27,-28,103,-19,-20,-21,-22,-23,-24,-25,-26,-14,-15,-16,-17,-18,]),'less_than':([42,44,45,47,48,50,51,61,62,83,89,90,91,92,93,94,95,96,97,126,127,128,129,],[-33,-12,-13,-31,-32,-29,-30,-27,-28,104,-19,-20,-21,-22,-23,-24,-25,-26,-14,-15,-16,-17,-18,]),'greater_than':([42,44,45,47,48,50,51,61,62,83,89,90,91,92,93,94,95,96,97,126,127,128,129,],[-33,-12,-13,-31,-32,-29,-30,-27,-28,105,-19,-20,-21,-22,-23,-24,-25,-26,-14,-15,-16,-17,-18,]),'elseif':([136,164,],[143,143,]),'else':([136,164,],[145,145,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ProgramFlow':([0,],[1,]),'VariablesDeclaration':([0,],[2,]),'SubroutinesDeclaration':([2,],[4,]),'SingleTypeVariableDeclaration':([3,18,],[6,40,]),'SimpleTypes':([3,18,],[7,7,]),'SingleSubroutine':([5,52,],[10,78,]),'SequenceOfIdentifiers':([7,19,21,66,],[13,41,49,86,]),'AssignmentStatement':([7,17,19,21,26,27,28,29,31,53,54,59,65,66,117,119,133,148,149,151,153,162,],[15,24,15,15,24,24,24,24,24,24,24,24,24,15,24,24,140,140,140,24,24,24,]),'Routine':([17,26,27,28,29,31,53,54,59,65,117,119,151,153,162,],[23,55,56,57,58,60,79,80,81,85,130,131,157,158,163,]),'UnaryOperation':([17,20,26,27,28,29,31,46,53,54,59,63,64,65,69,70,71,72,73,74,75,76,99,108,113,114,115,116,117,119,132,133,148,149,150,151,153,162,],[25,45,25,25,25,25,25,45,25,25,25,45,45,25,45,45,45,45,45,45,45,45,45,45,45,45,45,45,25,25,45,141,141,141,45,25,25,25,]),'ifCondition':([17,26,27,28,29,31,53,54,59,65,117,119,151,153,162,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'whileLoop':([17,26,27,28,29,31,53,54,59,65,117,119,151,153,162,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'doWhileLoop':([17,26,27,28,29,31,53,54,59,65,117,119,151,153,162,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'forLoop':([17,26,27,28,29,31,53,54,59,65,117,119,151,153,162,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'InOut':([17,26,27,28,29,31,53,54,59,65,117,119,151,153,162,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'ArithmeticExpression':([20,46,63,64,69,70,71,72,73,74,75,76,99,108,113,114,115,116,132,150,],[43,77,83,83,89,90,91,92,93,94,95,96,118,83,126,127,128,129,83,83,]),'Number':([20,46,63,64,69,70,71,72,73,74,75,76,99,108,113,114,115,116,132,150,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'BooleanExpression':([63,64,108,132,150,],[82,84,121,138,156,]),'LogicOperator':([83,],[99,]),'RecursiveIn':([87,122,],[110,134,]),'RecursiveOut':([88,124,],[112,135,]),'UpdateVariables':([133,148,149,],[139,154,155,]),'elseIfCondition':([136,164,],[142,165,]),'elseCondition':([136,164,],[144,144,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ProgramFlow","S'",1,None,None,None),
  ('ProgramFlow -> VariablesDeclaration SubroutinesDeclaration','ProgramFlow',2,'p_ProgramFlow','omega.py',141),
  ('AssignmentStatement -> identifier equal ArithmeticExpression','AssignmentStatement',3,'p_AssignmentStatement','omega.py',147),
  ('VariablesDeclaration -> Begin_Variables_Declaration SingleTypeVariableDeclaration End_Variables_Declaration','VariablesDeclaration',3,'p_VariablesDeclaration','omega.py',152),
  ('SingleTypeVariableDeclaration -> SimpleTypes SequenceOfIdentifiers semicolon SingleTypeVariableDeclaration','SingleTypeVariableDeclaration',4,'p_SingleTypeVariableDeclaration','omega.py',157),
  ('SingleTypeVariableDeclaration -> <empty>','SingleTypeVariableDeclaration',0,'p_SingleTypeVariableDeclaration','omega.py',158),
  ('SimpleTypes -> int','SimpleTypes',1,'p_SimpleTypes','omega.py',163),
  ('SimpleTypes -> double','SimpleTypes',1,'p_SimpleTypes','omega.py',164),
  ('SequenceOfIdentifiers -> identifier','SequenceOfIdentifiers',1,'p_SequenceOfIdentifiers','omega.py',169),
  ('SequenceOfIdentifiers -> identifier comma SequenceOfIdentifiers','SequenceOfIdentifiers',3,'p_SequenceOfIdentifiers','omega.py',170),
  ('SequenceOfIdentifiers -> AssignmentStatement','SequenceOfIdentifiers',1,'p_SequenceOfIdentifiers','omega.py',171),
  ('SequenceOfIdentifiers -> AssignmentStatement comma SequenceOfIdentifiers','SequenceOfIdentifiers',3,'p_SequenceOfIdentifiers','omega.py',172),
  ('ArithmeticExpression -> Number','ArithmeticExpression',1,'p_ArithmeticExpression','omega.py',177),
  ('ArithmeticExpression -> UnaryOperation','ArithmeticExpression',1,'p_ArithmeticExpression','omega.py',178),
  ('ArithmeticExpression -> open_parenthesis ArithmeticExpression close_parenthesis','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',179),
  ('ArithmeticExpression -> open_parenthesis ArithmeticExpression close_parenthesis plus ArithmeticExpression','ArithmeticExpression',5,'p_ArithmeticExpression','omega.py',180),
  ('ArithmeticExpression -> open_parenthesis ArithmeticExpression close_parenthesis minus ArithmeticExpression','ArithmeticExpression',5,'p_ArithmeticExpression','omega.py',181),
  ('ArithmeticExpression -> open_parenthesis ArithmeticExpression close_parenthesis star ArithmeticExpression','ArithmeticExpression',5,'p_ArithmeticExpression','omega.py',182),
  ('ArithmeticExpression -> open_parenthesis ArithmeticExpression close_parenthesis slash ArithmeticExpression','ArithmeticExpression',5,'p_ArithmeticExpression','omega.py',183),
  ('ArithmeticExpression -> Number plus ArithmeticExpression','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',184),
  ('ArithmeticExpression -> Number minus ArithmeticExpression','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',185),
  ('ArithmeticExpression -> Number star ArithmeticExpression','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',186),
  ('ArithmeticExpression -> Number slash ArithmeticExpression','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',187),
  ('ArithmeticExpression -> UnaryOperation plus ArithmeticExpression','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',188),
  ('ArithmeticExpression -> UnaryOperation minus ArithmeticExpression','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',189),
  ('ArithmeticExpression -> UnaryOperation star ArithmeticExpression','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',190),
  ('ArithmeticExpression -> UnaryOperation slash ArithmeticExpression','ArithmeticExpression',3,'p_ArithmeticExpression','omega.py',191),
  ('UnaryOperation -> plus_plus identifier','UnaryOperation',2,'p_UnaryOperation','omega.py',196),
  ('UnaryOperation -> minus_minus identifier','UnaryOperation',2,'p_UnaryOperation','omega.py',197),
  ('UnaryOperation -> identifier plus_plus','UnaryOperation',2,'p_UnaryOperation','omega.py',198),
  ('UnaryOperation -> identifier minus_minus','UnaryOperation',2,'p_UnaryOperation','omega.py',199),
  ('Number -> int_number','Number',1,'p_Number','omega.py',204),
  ('Number -> double_number','Number',1,'p_Number','omega.py',205),
  ('Number -> identifier','Number',1,'p_Number','omega.py',206),
  ('BooleanExpression -> ArithmeticExpression LogicOperator ArithmeticExpression','BooleanExpression',3,'p_BooleanExpression','omega.py',211),
  ('LogicOperator -> is_equal','LogicOperator',1,'p_LogicOperator','omega.py',216),
  ('LogicOperator -> not_equal','LogicOperator',1,'p_LogicOperator','omega.py',217),
  ('LogicOperator -> less_or_equal','LogicOperator',1,'p_LogicOperator','omega.py',218),
  ('LogicOperator -> greater_or_equal','LogicOperator',1,'p_LogicOperator','omega.py',219),
  ('LogicOperator -> less_than','LogicOperator',1,'p_LogicOperator','omega.py',220),
  ('LogicOperator -> greater_than','LogicOperator',1,'p_LogicOperator','omega.py',221),
  ('ifCondition -> if open_parenthesis BooleanExpression close_parenthesis open_brace Routine close_brace elseIfCondition','ifCondition',8,'p_ifCondition','omega.py',226),
  ('elseIfCondition -> elseif open_parenthesis BooleanExpression close_parenthesis open_brace Routine close_brace elseIfCondition','elseIfCondition',8,'p_elseIfCondition','omega.py',231),
  ('elseIfCondition -> elseCondition','elseIfCondition',1,'p_elseIfCondition','omega.py',232),
  ('elseCondition -> else open_brace Routine close_brace','elseCondition',4,'p_elseCondition','omega.py',237),
  ('elseCondition -> <empty>','elseCondition',0,'p_elseCondition','omega.py',238),
  ('whileLoop -> while open_parenthesis BooleanExpression close_parenthesis open_brace Routine close_brace','whileLoop',7,'p_whileLoop','omega.py',243),
  ('doWhileLoop -> do open_brace Routine close_brace while open_parenthesis BooleanExpression close_parenthesis semicolon','doWhileLoop',9,'p_doWhileLoop','omega.py',248),
  ('forLoop -> for open_parenthesis SequenceOfIdentifiers semicolon BooleanExpression semicolon UpdateVariables close_parenthesis open_brace Routine close_brace','forLoop',11,'p_forLoop','omega.py',253),
  ('UpdateVariables -> AssignmentStatement','UpdateVariables',1,'p_UpdateVariables','omega.py',257),
  ('UpdateVariables -> AssignmentStatement comma UpdateVariables','UpdateVariables',3,'p_UpdateVariables','omega.py',258),
  ('UpdateVariables -> UnaryOperation','UpdateVariables',1,'p_UpdateVariables','omega.py',259),
  ('UpdateVariables -> UnaryOperation comma UpdateVariables','UpdateVariables',3,'p_UpdateVariables','omega.py',260),
  ('Routine -> AssignmentStatement semicolon Routine','Routine',3,'p_Routine','omega.py',265),
  ('Routine -> UnaryOperation semicolon Routine','Routine',3,'p_Routine','omega.py',266),
  ('Routine -> ifCondition Routine','Routine',2,'p_Routine','omega.py',267),
  ('Routine -> whileLoop Routine','Routine',2,'p_Routine','omega.py',268),
  ('Routine -> doWhileLoop Routine','Routine',2,'p_Routine','omega.py',269),
  ('Routine -> forLoop Routine','Routine',2,'p_Routine','omega.py',270),
  ('Routine -> call identifier Routine','Routine',3,'p_Routine','omega.py',271),
  ('Routine -> InOut Routine','Routine',2,'p_Routine','omega.py',272),
  ('Routine -> <empty>','Routine',0,'p_Routine','omega.py',273),
  ('SubroutinesDeclaration -> Begin_Subroutines_Declaration SingleSubroutine End_Subroutines_Declaration','SubroutinesDeclaration',3,'p_SubroutinesDeclaration','omega.py',278),
  ('SingleSubroutine -> identifier open_brace Routine close_brace SingleSubroutine','SingleSubroutine',5,'p_SingleSubroutine','omega.py',283),
  ('SingleSubroutine -> <empty>','SingleSubroutine',0,'p_SingleSubroutine','omega.py',284),
  ('InOut -> cin in identifier RecursiveIn semicolon','InOut',5,'p_InOut','omega.py',289),
  ('InOut -> cout out identifier RecursiveOut semicolon','InOut',5,'p_InOut','omega.py',290),
  ('RecursiveIn -> in identifier RecursiveIn','RecursiveIn',3,'p_RecursiveIn','omega.py',295),
  ('RecursiveIn -> <empty>','RecursiveIn',0,'p_RecursiveIn','omega.py',296),
  ('RecursiveOut -> out identifier RecursiveOut','RecursiveOut',3,'p_RecursiveOut','omega.py',301),
  ('RecursiveOut -> <empty>','RecursiveOut',0,'p_RecursiveOut','omega.py',302),
]
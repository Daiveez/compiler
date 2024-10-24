import ply.yacc as yacc
# from lexer import tokens
# from my_ast import Number, Subtract, Print, Add
#
# # Parser rules
# class Parser:
#     def p_expression_plus(p):
#         'expression : expression PLUS term'
#         p[0] = BinaryOperations(p[1], p[3])
#
#     def p_expression_minus(p):
#         'expression : expression MINUS term'
#         p[0] = BinaryOperations(p[1], p[3])
#
#     def p_expression_term(p):
#         'expression : term'
#         p[0] = p[1]
#
#     def p_term_number(p):
#         'term : NUMBER'
#         p[0] = Literal(p[1], 'int')
#
#     def p_error(p):
#         print("Syntax error in input!")
#
# # Build the parser
# parser = yacc.yacc()
#
# # AST nodes
# class Node:
#     def __init__(self, children=[]):
#         self.children = children
#
# class Assignment(Node):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#         super().__init__([left, right])
#
# class BinaryOperations(Node):
#     def __init__(self, left, right):
#         self.left = left
#         self.right = right
#         super().__init__([left, right])
#
# class Literal(Node):
#     def __init__(self, value, type):
#         self.value = value
#         self.type = type
#         super().__init__()
#
# # Semantic Analyzer
# class SemanticAnalyzer:
#     def __init__(self):
#         self.symbol_table = {}
#
#     def visit(self, node):
#         method_name = f'visit_{type(node).__name__}'
#         visitor = getattr(self, method_name, self.generic_visit)
#         return visitor(node)
#
#     def generic_visit(self, node):
#         for child in node.children:
#             self.visit(child)
#
#     def visit_Assignment(self, node):
#         var_name = node.left.value
#         var_type = self.visit(node.right)
#         self.symbol_table[var_name] = var_type
#
#     def visit_BinaryOperations(self, node):
#         left = self.visit(node.left)
#         right = self.visit(node.right)
#         if left != right:
#             raise Exception("Type mismatch")
#         return left
#
#     def visit_Literal(self, node):
#         return node.type
#
# # Example usage
# data = "3 + 4"
# ast = parser.parse(data)
# if ast is None:
#     print("Parsing failed.")
# else:
#     semantic_analyzer = SemanticAnalyzer()
#     semantic_analyzer.visit(ast)

from rply import ParserGenerator
from my_ast import Number, Add, Subtract, Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB']
        )

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Add(left, right)
            elif operator.gettokentype() == 'SUB':
                return Subtract(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
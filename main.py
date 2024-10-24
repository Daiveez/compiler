from lexer import Lexer
from parser import Parser
from codegen import CodeGen

text = """
print(4 + 4 - 3);
"""
lexer = Lexer().get_lexer()
tokens = lexer.lex(text)

codegen = CodeGen()

pg = Parser()
pg.parse()
parser = pg.get_parser()
ast = parser.parse(tokens)
if ast is None:
    print("Parsing failed.")
else:
    ast.eval()

for token in tokens:
    print(token)
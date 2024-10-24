import ply.lex as lex
from rply import LexerGenerator
# adding Reserved words
reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
    'for' : 'FOR',
    'do' : 'DO',
    'break' : 'BREAK',
}

# List of token names
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'ASSIGN',
    'COMMENT',
    'CCODE',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule for identifiers and reserved words
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Declare the state
states = (
    ('comment', 'exclusive'),
)

# Match the first { and enter the comment state
def t_comment(t):
    r'\{'
    t.lexer.code_start = t.lexer.lexpos
    t.lexer.level = 1
    t.lexer.begin('comment')

# Rules for the comment state
def t_comment_lbrace(t):
    r'\{'
    t.lexer.level += 1

def t_comment_rbrace(t):
    r'\}'
    t.lexer.level -= 1

    if t.lexer.level == 0:
        t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos+1]
        t.type = 'COMMENT'
        t.lexer.lineno += t.value.count('\n')
        t.lexer.begin('INITIAL')
        return t

# C or C++ comment (ignore)
def t_comment_C(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

# C string
def t_ccode_string(t):
    r'\"([^\\\n]|(\\.))*?\"'

# C character literal
def t_ccode_char(t):
    r'\'([^\\\n]|(\\.))*?\''

# Any sequence of non-whitespace characters (not braces, strings)
def t_ccode_nonspace(t):
    r'[^\s\{\}\'\"]+'

# Ignored characters (whitespace)
t_comment_ignore = " \t\n"

# For bad characters, we just skip over it
def t_comment_error(t):
    r'.'
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
a = 3 + 4 * 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

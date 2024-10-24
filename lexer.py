import ply.lex as lex

class Lexer:
    def __init__(self):
        self.tokens = [
            'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'ID', 'ASSIGN', 'COMMENT', 'CCODE'
        ]
        self.reserved = {
            'if': 'IF', 'then': 'THEN', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR', 'do': 'DO', 'break': 'BREAK'
        }
        self.tokens += list(self.reserved.values())
        self.lexer = lex.lex(module=self)

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_ASSIGN = r'='

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    states = (('comment', 'exclusive'),)

    def t_comment(self, t):
        r'\{'
        t.lexer.code_start = t.lexer.lexpos
        t.lexer.level = 1
        t.lexer.begin('comment')

    def t_comment_lbrace(self, t):
        r'\{'
        t.lexer.level += 1

    def t_comment_rbrace(self, t):
        r'\}'
        t.lexer.level -= 1
        if t.lexer.level == 0:
            t.value = t.lexer.lexdata[t.lexer.code_start:t.lexer.lexpos+1]
            t.type = 'COMMENT'
            t.lexer.lineno += t.value.count('\n')
            t.lexer.begin('INITIAL')
            return t

    def t_comment_C(self, t):
        r'(/\*(.|\n)*?\*/)|(//.*)'
        pass

    t_comment_ignore = " \t\n"

    def t_comment_error(self, t):
        r'.'
        t.lexer.skip(1)

    def input(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def get_lexer(self):
        return self.lexer

from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any, Iterator, List
from string import digits

class TokenType(StrEnum):
    INT = auto()
    FLOAT = auto()
    IDENTIFIER = auto()
    PRINT = auto()
    LPAREN = auto()
    RPAREN = auto()
    COLON = auto()
    COMMA = auto()
    ASSIGN = auto()
    NEWLINE = auto()
    LOOP = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    EXPONENT = auto()
    MODULO = auto()
    LESSTHAN = auto()
    COMMENT = auto()
    STRING = auto()
    FSTRING = auto()
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: Any = None

class Tokenizer:
    def __init__(self, code: str) -> None:
        self.code = code
        self.ptr: int = 0
        self.indentation_stack: List[int] = [0]  
        self.current_indentation: int = 0

    def next_token(self) -> Token:
        while self.ptr < len(self.code) and self.code[self.ptr] == " ":
            self.ptr += 1

        if self.ptr == len(self.code):
            return Token(TokenType.EOF)

        char = self.code[self.ptr]

        # Handle identifiers and keywords
        if char.isalpha() or char == "_":
            start_ptr = self.ptr
            while (self.ptr < len(self.code) and 
                   (self.code[self.ptr].isalnum() or self.code[self.ptr] == "_")):
                self.ptr += 1
            value = self.code[start_ptr:self.ptr]
            if value == "print":
                return Token(TokenType.PRINT)
            if value == "while":
                return Token(TokenType.LOOP)
            return Token(TokenType.IDENTIFIER, value)

        # Handle single character tokens
        if char == ":":
            self.ptr += 1
            return Token(TokenType.COLON)

        if char == ",":
            self.ptr += 1
            return Token(TokenType.COMMA)

        if char == "=":
            self.ptr += 1
            return Token(TokenType.ASSIGN)

        if char == "(":
            self.ptr += 1
            return Token(TokenType.LPAREN)

        if char == ")":
            self.ptr += 1
            return Token(TokenType.RPAREN)

        if char == "+":
            self.ptr += 1
            return Token(TokenType.PLUS)
        elif char == "-":
            self.ptr += 1
            return Token(TokenType.MINUS)
        elif char == "*":
            if self.ptr + 1 < len(self.code) and self.code[self.ptr + 1] == "*":
                self.ptr += 2 
                return Token(TokenType.EXPONENT) 
            else:
                self.ptr += 1
                return Token(TokenType.MULTIPLY)
        elif char == "/":
            self.ptr += 1
            return Token(TokenType.DIVIDE)
        elif char == "%":
            self.ptr += 1
            return Token(TokenType.MODULO)
        elif char == "<":
            self.ptr += 1
            return Token(TokenType.LESSTHAN)

        if char in digits:  # Handle integers and floats
            start_ptr = self.ptr
            while self.ptr < len(self.code) and self.code[self.ptr] in digits:
                self.ptr += 1

            if self.ptr < len(self.code) and self.code[self.ptr] == ".":
                self.ptr += 1 

                while self.ptr < len(self.code) and self.code[self.ptr] in digits:
                    self.ptr += 1

                return Token(TokenType.FLOAT, float(self.code[start_ptr:self.ptr]))

            return Token(TokenType.INT, int(self.code[start_ptr:self.ptr]))


        if char == "#":  # Handle comments
            while self.ptr < len(self.code) and self.code[self.ptr] != "\n":
                self.ptr += 1
            return self.next_token()  # Skip the comment and move to the next token


        if char == "\n":  # Handle newlines
            self.ptr += 1
            current_indent_level = self.indentation_stack[-1]  # Current indentation level
            
            # Check for indentation
            new_indent_level = 0
            while self.ptr < len(self.code) and self.code[self.ptr] == " ":
                new_indent_level += 1
                self.ptr += 1
            
            if new_indent_level > current_indent_level:
                self.indentation_stack.append(new_indent_level)
                return Token(TokenType.INDENT)
            elif new_indent_level < current_indent_level:
                # Dedent logic
                while self.indentation_stack and self.indentation_stack[-1] > new_indent_level:
                    self.indentation_stack.pop()
                    return Token(TokenType.DEDENT)
                
            return Token(TokenType.NEWLINE)

        if char in ('"', "'"):  # Handle string literals
            quote_type = char
            start_ptr = self.ptr
            self.ptr += 1  # Move past the opening quote

            # Check for f-string
            is_fstring = False
            if start_ptr > 0 and self.code[start_ptr - 1] in ('f', 'F'):
                is_fstring = True
                
            while self.ptr < len(self.code) and self.code[self.ptr] != quote_type:
                if self.code[self.ptr] == "\\":
                    self.ptr += 2  # Skip escaped character
                else:
                    self.ptr += 1
                
            if self.ptr < len(self.code):
                self.ptr += 1  # Move past the closing quote
                
            value = self.code[start_ptr:self.ptr]
            if is_fstring:
                return Token(TokenType.FSTRING, value)
            return Token(TokenType.STRING, value)

        # Handle unexpected characters
        raise RuntimeError(f"Can't tokenize {char!r} at position {self.ptr}.")

    def __iter__(self) -> Iterator[Token]:
        while (token := self.next_token()).type != TokenType.EOF:
            yield token
        yield token  # Yield the EOF token too.

# Getting tokens
def tokens():
    with open ("source_code.txt", "r") as file:
        code = file.read()
    tokens = []
    tokenizer = Tokenizer(code)
    for token in tokenizer:
        tokens.append(token)
        print(token)


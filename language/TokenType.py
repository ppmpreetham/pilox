from enum import Enum, auto

class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE, COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR = auto()
    
    # One or two character tokens
    BANG, BANG_EQUAL, EQUAL, EQUAL_EQUAL, GREATER, GREATER_EQUAL, LESS, LESS_EQUAL = auto()
    
    # Literals
    IDENTIFIER, STRING, NUMBER = auto()
    
    # Keywords
    AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR, PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE, EOF = auto()

class Token:
    """A class representing a token in the source code."""
    
    def __init__(self, type: TokenType, lexeme: str, literal: str, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
        
    def __repr__(self):
        return f"{self.type} {self.lexeme} {self.literal}"

from typing import List, Tuple, Union, Optional
from TokenType import *

class Scanner:
    
    tokens: Token = []
    start: int = 0
    current: int = 0
    line: int = 1
    source = ""
    
    def __init__(self, source: str):
        """Scans a given source code and returns a list of tokens.

        Args:
            source (str): the source code to be scanned
        """
        self.source = source
        
    def scanTokens(self) -> List[Token]:
        """Scans the tokens in the source code.
        
        Returns:
            List[Token]: a list of tokens found in the source code
        """
        self.start = 0
        self.current = 0
        self.tokens = []
        
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        
        return self.tokens
        
    def isAtEnd(self) -> bool:
        """Check if we've reached the end of the source code.

        Returns:
            bool: True if at the end of source, False otherwise
        """
        return self.current >= len(self.source)
    
    def advance(self):
        self.current += 1
        return self.source[self.current-1]
    
    
    def scanToken(self):
        c = self.advance()
        match c:
            case '(':
                self.addToken(TokenType.LEFT_PAREN)
            case ')':
                self.addToken(TokenType.RIGHT_PAREN)
            case '{':
                self.addToken(TokenType.LEFT_BRACE)
            case '}':
                self.addToken(TokenType.RIGHT_BRACE)
            case ',':
                self.addToken(TokenType.COMMA)
            case '.':
                self.addToken(TokenType.DOT)
            case '-':
                self.addToken(TokenType.MINUS)
            case '+':
                self.addToken(TokenType.PLUS)
            case ';':
                self.addToken(TokenType.SEMICOLON)
            case '*':
                self.addToken(TokenType.STAR)
                
    def addToken(self, type: TokenType, literal: object):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))
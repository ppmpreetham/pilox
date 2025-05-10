from typing import List, Tuple, Union, Optional
from TokenType import *

class Scanner:
    
    tokens: Token = []
    start: int = 0
    current: int = 0
    line: int = 1
    source = ""
    
    def __init__(self, source: str):
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
    
    def peek(self):
        """Get the next character without advancing the current position."""
        return '\0' if self.isAtEnd() else self.source[self.current]
    
    def scanToken(self):
        c = self.advance()
        match c:
            case '|':
                self.addToken(TokenType.PIPE)
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
            case '!':
                # self.twoPairCheck('=', TokenType.BANG, TokenType.BANG_EQUAL)
                self.addToken(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case '=':
                # self.twoPairCheck('=', TokenType.EQUAL, TokenType.EQUAL_EQUAL)
                self.addToken(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<':
                # self.twoPairCheck('=', TokenType.LESS, TokenType.LESS_EQUAL)
                self.addToken(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case '>':
                # self.twoPairCheck('=', TokenType.GREATER, TokenType.GREATER_EQUAL)
                self.addToken(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass
            case '\n':
                self.line += 1
            case '/':
                if self.match('/'):
                    while not self.isAtEnd() and self.source[self.current] != '\n':
                        self.advance()
                else:
                    self.addToken(TokenType.SLASH)
            case _:
                print("UNEXPECTED CHARACTER, PILO IS ANGY NOW!!")
    
    def match(self, expected: str) -> bool:
        """Check if the next character matches the expected character.

        Args:
            expected (str): the expected character

        Returns:
            bool: True if it matches, False otherwise
        """
        if self.isAtEnd() or self.source[self.current] != expected:
            return False
        self.current += 1
        return True
    
    # NOT USING THIS FUNCTION ANYMORE, KEEP IT FOR FUTURE REFERENCE
    def twoPairCheck(self, char: str, first: TokenType, second: TokenType):
        """Check if the character is a two-pair character and add the appropriate token.

        Args:
            char (str): the character to check
            first (TokenType): the token type if no match
            second (TokenType): the token type if matched
        """
        if not self.isAtEnd() and self.source[self.current] == char:
            self.current += 1
            self.addToken(second)
        else:
            self.addToken(first)
    
    def addToken(self, type: TokenType, literal: object = None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))
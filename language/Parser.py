from TokenType import *
from typing import Any, List
from Expr import Expr, Binary

class Parser:
    """Parser for the Pilox language."""
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    
    def expression(self) -> Expr:
        """expression → equality ;"""
        return self.equality()
    
    def equality(self) -> Expr:
        """equality → comparision ( ( "!=" | "==" ) comparision )* ;"""
        expr: Expr = self.comparision() # just comparison (a)

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator: Token = self.previous() # operator token
            right: Expr = self.comparision() # right side of the operator
            expr = Binary(left=expr, operator=operator, right=right) # example: a == b

        return expr
    
    def comparision(self) -> Expr:
        """comparision → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;"""
        expr: Expr = self.term()
        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL, TokenType.LESS, TokenType.LESS_EQUAL):
            operator: Token = self.previous()
            right: Token = self.term()
            expr = Binary(left=expr, operator=operator, right=right)
        
        return expr
    
    def term(self) -> Expr:
        """term → factor ( ( "-" | "+" ) factor )* ;"""
        expr: Expr = self.factor()
        
        while(self.match(TokenType.MINUS, TokenType.PLUS)):
            operator: TokenType = self.previous()
            right: TokenType = self.factor()
            expr = Binary(left=expr, operator=operator, right=right)
        
        return expr
    
    def factor(self) -> Expr:
        """factor → unary ( ( "/" | "*" ) unary )* ;"""
        expr: Expr = self.unary()
        
        while(self.match(TokenType.SLASH, TokenType.STAR)):
            operator: TokenType = self.previous()
            right: TokenType = self.unary()
            expr = Binary(left=expr, operator=operator, right=right)
        
        return expr
        
    # Helper Methods
    def match(self, *types: TokenType) -> bool:
        """Check if the next token is of the specified type(s) and consume it."""
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False
    
    def check(self, token_type: TokenType) -> bool:
        if self.isAtEnd():
            return False
        return type(self.peek()) == token_type
    
    def advance(self) -> Token:
        """Consume the next token and return it."""
        if not self.isAtEnd():
            self.current += 1
        return self.previous()
    
    def isAtEnd(self) -> bool:
        """Check if the parser has reached the end of the token list."""
        return self.peek().type == TokenType.EOF
    
    def peek(self) -> Token:
        """Return the next token without consuming it."""
        return self.tokens[self.current]
    
    def previous(self) -> Token:
        """Return the previous token."""
        return self.tokens[self.current - 1] if self.current > 0 else None
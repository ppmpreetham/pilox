from TokenType import *
from typing import Any, List
from Expr import Expr

class Parser:
    """Parser for the Pilox language."""
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
    
    def expression(self) -> Expr:
        """expression → equality ;"""
        return self.equality()
    
    def equality(self) -> Expr:
        """equality → comparison ( ( "!=" | "==" ) comparison )* ;"""
        expr: Expr = self.comparison() # just comparison (a)

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator: Token = self.previous() # operator token
            right: Expr = self.comparison() # right side of the operator
            expr = Expr.Binary(left=expr, operator=operator, right=right) # example: a == b

        return expr
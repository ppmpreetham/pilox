from typing import List, Tuple, Union, Optional
from language.TokenType import *

class Scanner:
    
    tokens: Token = []
    
    def __init__(self, source: str):
        """scans a given source code and returns a list of tokens.

        Args:
            source (str): the source code to be scanned
        """
        self.source = source
        
    def scanTokens(self) -> List[Token]:
        """scans the tokens in the source code.
        
        Returns:
            List[Token]: a list of tokens found in the source code
        """
        self.start = 0
        self.current = 0
        self.tokens = []
        
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        
        self.tokens.append(Token(TokenType.EOF, "", None, 0))
        
        return self.tokens
        
    def isAtEnd(self) -> bool:
        """Check if we've reached the end of the source code.

        Returns:
            bool: True if at the end of source, False otherwise
        """
        return self.current >= len(self.source)
    
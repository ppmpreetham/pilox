from typing import Any
from Expr import Expr, Binary, Grouping, Literal, Unary, ExprVisitor
from TokenType import TokenType, Token

class ASTPrinter(ExprVisitor):
    """Prints an AST in a lisp-like notation."""
    
    def print(self, expr: Expr) -> str:
        """Print the expression as a string."""
        return expr.accept(self)

    def visit_binaryexpr(self, expr: Binary) -> str:
        """Visit a binary expression."""
        return self.parenthesize(
            expr.operator.lexeme, expr.left, expr.right
        )

    def visit_groupingexpr(self, expr: Grouping) -> str:
        """Visit a grouping expression."""
        return self.parenthesize("group", expr.expression)  

    def visit_literalexpr(self, expr: Literal) -> str:
        """Visit a literal expression."""
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visit_unaryexpr(self, expr: Unary) -> str:
        """Visit a unary expression."""
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs: Expr) -> str:
        """Helper method to format expressions in parentheses."""
        result = "(" + name

        for expr in exprs:
            result += " "
            result += expr.accept(self)

        result += ")"

        return result

if __name__ == "__main__":
    # Example usage
    expression = Binary(
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal(123)
        ),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(
            Literal(45.67)
        )
    )
    printer = ASTPrinter()
    print(printer.print(expression))
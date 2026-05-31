# calc_engine.py
from __future__ import annotations
from lark import Lark, Transformer, v_args

GRAMMAR = r"""
?start: expr

?expr: expr "+" term   -> add
     | expr "-" term   -> sub
     | term

?term: term "*" factor -> mul
     | term "/" factor -> div
     | factor

?factor: "-" factor    -> neg
       | atom

?atom: NUMBER          -> number
     | atom "%"        -> percent
     | "(" expr ")"

%import common.SIGNED_NUMBER -> NUMBER
%import common.WS_INLINE
%ignore WS_INLINE
"""

@v_args(inline=True)
class _CalcTransformer(Transformer):
    def number(self, tok):
        # tok is like "12", "-3.5"
        return float(tok)

    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b

    def neg(self, a): return -a

    def percent(self, a):
        # calculator-style percent: "50%" => 0.5
        return a / 100.0


class CalculatorEngine:
    """
    Safe expression evaluator using Lark.

    Supports:
      - parentheses
      - + - * /
      - unary minus
      - percent postfix: 10% => 0.1
    """
    def __init__(self):
        self._parser = Lark(GRAMMAR, parser="lalr", transformer=_CalcTransformer())

    def eval(self, expr: str) -> float:
        expr = expr.strip()
        if not expr:
            return 0.0
        # Normalize common calculator symbols to grammar
        expr = (expr
                .replace("×", "*")
                .replace("÷", "/")
                .replace("−", "-"))
        return float(self._parser.parse(expr))

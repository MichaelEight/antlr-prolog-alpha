from antlr4 import *
from MiniPrologLexer import MiniPrologLexer
from MiniPrologParser import MiniPrologParser

input_text = """
parent(john, mary).
parent(mary, alice).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
?- grandparent(john, alice).
"""

input_stream = InputStream(input_text)
lexer = MiniPrologLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = MiniPrologParser(token_stream)

tree = parser.program()
print(tree.toStringTree(recog=parser))

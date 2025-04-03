# Generated from MiniProlog.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniPrologParser import MiniPrologParser
else:
    from MiniPrologParser import MiniPrologParser

# This class defines a complete generic visitor for a parse tree produced by MiniPrologParser.

class MiniPrologVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniPrologParser#program.
    def visitProgram(self, ctx:MiniPrologParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPrologParser#statement.
    def visitStatement(self, ctx:MiniPrologParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPrologParser#fact.
    def visitFact(self, ctx:MiniPrologParser.FactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPrologParser#rule.
    def visitRule(self, ctx:MiniPrologParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPrologParser#query.
    def visitQuery(self, ctx:MiniPrologParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPrologParser#atomList.
    def visitAtomList(self, ctx:MiniPrologParser.AtomListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPrologParser#atom.
    def visitAtom(self, ctx:MiniPrologParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPrologParser#args.
    def visitArgs(self, ctx:MiniPrologParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPrologParser#term.
    def visitTerm(self, ctx:MiniPrologParser.TermContext):
        return self.visitChildren(ctx)



del MiniPrologParser
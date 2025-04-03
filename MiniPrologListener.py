# Generated from MiniProlog.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniPrologParser import MiniPrologParser
else:
    from MiniPrologParser import MiniPrologParser

# This class defines a complete listener for a parse tree produced by MiniPrologParser.
class MiniPrologListener(ParseTreeListener):

    # Enter a parse tree produced by MiniPrologParser#program.
    def enterProgram(self, ctx:MiniPrologParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#program.
    def exitProgram(self, ctx:MiniPrologParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniPrologParser#statement.
    def enterStatement(self, ctx:MiniPrologParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#statement.
    def exitStatement(self, ctx:MiniPrologParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniPrologParser#fact.
    def enterFact(self, ctx:MiniPrologParser.FactContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#fact.
    def exitFact(self, ctx:MiniPrologParser.FactContext):
        pass


    # Enter a parse tree produced by MiniPrologParser#rule.
    def enterRule(self, ctx:MiniPrologParser.RuleContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#rule.
    def exitRule(self, ctx:MiniPrologParser.RuleContext):
        pass


    # Enter a parse tree produced by MiniPrologParser#query.
    def enterQuery(self, ctx:MiniPrologParser.QueryContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#query.
    def exitQuery(self, ctx:MiniPrologParser.QueryContext):
        pass


    # Enter a parse tree produced by MiniPrologParser#atomList.
    def enterAtomList(self, ctx:MiniPrologParser.AtomListContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#atomList.
    def exitAtomList(self, ctx:MiniPrologParser.AtomListContext):
        pass


    # Enter a parse tree produced by MiniPrologParser#atom.
    def enterAtom(self, ctx:MiniPrologParser.AtomContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#atom.
    def exitAtom(self, ctx:MiniPrologParser.AtomContext):
        pass


    # Enter a parse tree produced by MiniPrologParser#args.
    def enterArgs(self, ctx:MiniPrologParser.ArgsContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#args.
    def exitArgs(self, ctx:MiniPrologParser.ArgsContext):
        pass


    # Enter a parse tree produced by MiniPrologParser#term.
    def enterTerm(self, ctx:MiniPrologParser.TermContext):
        pass

    # Exit a parse tree produced by MiniPrologParser#term.
    def exitTerm(self, ctx:MiniPrologParser.TermContext):
        pass



del MiniPrologParser
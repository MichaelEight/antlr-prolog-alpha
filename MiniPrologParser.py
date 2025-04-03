# Generated from MiniProlog.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,9,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,1,
        1,1,3,1,30,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,5,5,47,8,5,10,5,12,5,50,9,5,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,5,7,60,8,7,10,7,12,7,63,9,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,
        12,14,16,0,0,62,0,21,1,0,0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,34,1,0,
        0,0,8,39,1,0,0,0,10,43,1,0,0,0,12,51,1,0,0,0,14,56,1,0,0,0,16,64,
        1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,
        21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,0,0,1,25,1,1,0,
        0,0,26,30,3,4,2,0,27,30,3,6,3,0,28,30,3,8,4,0,29,26,1,0,0,0,29,27,
        1,0,0,0,29,28,1,0,0,0,30,3,1,0,0,0,31,32,3,12,6,0,32,33,5,1,0,0,
        33,5,1,0,0,0,34,35,3,12,6,0,35,36,5,2,0,0,36,37,3,10,5,0,37,38,5,
        1,0,0,38,7,1,0,0,0,39,40,5,3,0,0,40,41,3,10,5,0,41,42,5,1,0,0,42,
        9,1,0,0,0,43,48,3,12,6,0,44,45,5,4,0,0,45,47,3,12,6,0,46,44,1,0,
        0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,11,1,0,0,0,50,48,
        1,0,0,0,51,52,5,7,0,0,52,53,5,5,0,0,53,54,3,14,7,0,54,55,5,6,0,0,
        55,13,1,0,0,0,56,61,3,16,8,0,57,58,5,4,0,0,58,60,3,16,8,0,59,57,
        1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,15,1,0,0,0,
        63,61,1,0,0,0,64,65,5,7,0,0,65,17,1,0,0,0,4,21,29,48,61
    ]

class MiniPrologParser ( Parser ):

    grammarFileName = "MiniProlog.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "':-'", "'?-'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_fact = 2
    RULE_rule = 3
    RULE_query = 4
    RULE_atomList = 5
    RULE_atom = 6
    RULE_args = 7
    RULE_term = 8

    ruleNames =  [ "program", "statement", "fact", "rule", "query", "atomList", 
                   "atom", "args", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    WS=8
    COMMENT=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniPrologParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPrologParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniPrologParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniPrologParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniPrologParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==7:
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(MiniPrologParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(MiniPrologParser.FactContext,0)


        def rule_(self):
            return self.getTypedRuleContext(MiniPrologParser.RuleContext,0)


        def query(self):
            return self.getTypedRuleContext(MiniPrologParser.QueryContext,0)


        def getRuleIndex(self):
            return MiniPrologParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniPrologParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.fact()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.rule_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.query()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(MiniPrologParser.AtomContext,0)


        def getRuleIndex(self):
            return MiniPrologParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = MiniPrologParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fact)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.atom()
            self.state = 32
            self.match(MiniPrologParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(MiniPrologParser.AtomContext,0)


        def atomList(self):
            return self.getTypedRuleContext(MiniPrologParser.AtomListContext,0)


        def getRuleIndex(self):
            return MiniPrologParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = MiniPrologParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.atom()
            self.state = 35
            self.match(MiniPrologParser.T__1)
            self.state = 36
            self.atomList()
            self.state = 37
            self.match(MiniPrologParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomList(self):
            return self.getTypedRuleContext(MiniPrologParser.AtomListContext,0)


        def getRuleIndex(self):
            return MiniPrologParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = MiniPrologParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(MiniPrologParser.T__2)
            self.state = 40
            self.atomList()
            self.state = 41
            self.match(MiniPrologParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPrologParser.AtomContext)
            else:
                return self.getTypedRuleContext(MiniPrologParser.AtomContext,i)


        def getRuleIndex(self):
            return MiniPrologParser.RULE_atomList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomList" ):
                listener.enterAtomList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomList" ):
                listener.exitAtomList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomList" ):
                return visitor.visitAtomList(self)
            else:
                return visitor.visitChildren(self)




    def atomList(self):

        localctx = MiniPrologParser.AtomListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atomList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.atom()
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 44
                self.match(MiniPrologParser.T__3)
                self.state = 45
                self.atom()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniPrologParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(MiniPrologParser.ArgsContext,0)


        def getRuleIndex(self):
            return MiniPrologParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = MiniPrologParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MiniPrologParser.ID)
            self.state = 52
            self.match(MiniPrologParser.T__4)
            self.state = 53
            self.args()
            self.state = 54
            self.match(MiniPrologParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPrologParser.TermContext)
            else:
                return self.getTypedRuleContext(MiniPrologParser.TermContext,i)


        def getRuleIndex(self):
            return MiniPrologParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = MiniPrologParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.term()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 57
                self.match(MiniPrologParser.T__3)
                self.state = 58
                self.term()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniPrologParser.ID, 0)

        def getRuleIndex(self):
            return MiniPrologParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MiniPrologParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MiniPrologParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






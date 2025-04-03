grammar MiniProlog;

program     : statement* EOF ;

statement
    : fact
    | rule
    | query
    ;

fact        : atom '.' ;
rule        : atom ':-' atomList '.' ;
query       : '?-' atomList '.' ;

atomList    : atom (',' atom)* ;

atom        : ID '(' args ')' ;
args        : term (',' term)* ;
term        : ID ;

ID          : [a-zA-Z_][a-zA-Z_0-9]* ;
WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '%' ~[\r\n]* -> skip ;

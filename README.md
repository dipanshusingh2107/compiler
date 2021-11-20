# compiler
This is a basic compiler 

Our Language will support:

Numerical variables
Basic arithmetic
If statements
While loops
Print text and numbers
Input numbers
Labels and goto
Comments


Operator : + - * / = == != > < >= <=
Keyword: LABEL, GOTO, PRINT, INPUT, LET, IF, THEN, ENDIF, WHILE, REPEAT, ENDWHILE
Identifier. An alphabetical character followed by zero or more alphanumeric characters.
Numbers 

# GRAMMAR

program ::= {statement}
statement ::= "PRINT" (expression | string) nl
expression ::= term {( "-" | "+" ) term}
term ::= unary {( "/" | "*" ) unary}
unary ::= primary
primary ::= ["+" | "-"] (number | ident)
nl ::= '\n'+

# Notation of Grammar

{} means zero or more 
[] means zero or one 
+ means one or more of whatever is to the left
() is just for grouping
| is a logical or.


# Bugs


# Not Supported Grammar

statement ::= "IF" comparison "THEN" nl {statement} "ENDIF" nl
            | "WHILE" comparison "REPEAT" nl {statement} "ENDWHILE" nl
            | "LABEL" ident nl
            | "GOTO" ident nl
            | "LET" ident "=" expression nl
            | "INPUT" ident nl
comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
unary ::= ["+" | "-"] primary
primary ::= number | ident

    


from enum import Flag
from tokens import TokenType
import sys

class Parser():
    def __init__(self , token) :    #Needed tokens from the lexer
        self.token = token
        self.currTokenPos = 0
        self.numberOfTokens = len(token)
    
    def increasePos(self , step = 1):
        self.currTokenPos+=step
    def decreasePos(self , step =1):
        self.currTokenPos-=step
    
    def currToken(self):
        return self.token[self.currTokenPos]
    
    def getToken(self , pos = 0):   #this is also crap
        if self.currTokenPos+pos >= self.numberOfTokens:
            return False
        return self.token[self.currTokenPos + pos]

    def program(self):
        print("Program Parsing begins!")
        while(self.currTokenPos < self.numberOfTokens):
            self.statements()
        print("Parsing Completed")
    
    def nl(self):       #some error here this is crap
        flag = False
        while(self.currToken() == TokenType.NEWLINE):
            print("NEW LINE")
            self.increasePos()
            flag = True
        return flag

    def statements(self):
        if self.nl():
            return True

        if self.currToken() == TokenType.EOF:
            self.increasePos()
            return True

        if self.currToken() == TokenType.PRINT:
            print('STATEMENT PRINT')
            self.increasePos()
            if self.currToken() == TokenType.STRING:    #PRINT "STRING"

                self.increasePos()
                if self.currToken() == TokenType.NEWLINE:
                    self.nl()
                    return True
                else:
                    sys.exit('SYNTAX ERROR New line not found after string')
            else:           #PRINT EXPRESSION
                if self.expression() == False:
                    sys.exit('SYNTAX ERROR NO Expression or string found after PRINT')
                elif self.currToken() != TokenType.NEWLINE:
                    print("Token Found " ,self.currToken())
                    sys.exit('SYNTAX ERROR New line not found after Expression')
        else:
            print("Token Found " ,self.currToken())
            sys.exit('SYNTAX ERROR Statement is not a print statement')
    

    def expression(self):
        print("CHECKING EXPRESSION")
        if self.term():
            while self.currToken() == TokenType.MINUS or self.currToken() == TokenType.PLUS:
                print("Token Found " ,self.currToken())
                self.increasePos()
                if self.term() == False:
                    sys.exit('SYNTAX ERROR NOTHING FOUND AFTER +/-')
                    return False
            return True
        else:
            sys.exit('SYNTAX ERROR NOT AN EXPRESSION FIRST TOKEN IS NOT TERM')
            return False

    def term(self):
        print("CHECKING TERM")
        if self.unary():
            while self.currToken() == TokenType.SLASH or self.currToken() == TokenType.ASTERISK:
                print("Token Found " ,self.currToken())
                self.increasePos()
                if self.unary() == False:
                    sys.exit('SYNTAX ERROR NOT UNIARY AFTER / *')
                    flag = False
            return True
        else:
            sys.exit('SYNTAX ERROR')
            return False

    def unary(self):
        print("CHECKING UNARY")
        if(self.primary()):
            return True
        elif self.currToken() == TokenType.PLUS or self.currToken() == TokenType.MINUS:
            print("Token Found " ,self.currToken())
            self.increasePos()
            if (self.primary()):
                return True
            else:
                sys.exit('SYNTAX ERROR NOT A UNIARY')
                return False
        else:
            sys.exit('SYNTAX ERROR')
            return False

    
    def primary(self):
        print("CHECKING PRIMARY")
        if self.currToken() == TokenType.IDENT:
            print("Token Found " ,self.currToken())
            self.increasePos()
            return True
        elif self.currToken() == TokenType.NUMBER:
            print("Token Found " ,self.currToken())
            self.increasePos()
            return True
        else:
            sys.exit('SYNTAX ERROR')
            return False    #useless part execution terminates

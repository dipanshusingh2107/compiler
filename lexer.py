from tokens import TokenType
class lexer():
    def __init__(self , input):
        self.input = input
        self.length = len(input)
        self.currPos = 0

    def currChar(self):
        return self.input[self.currPos]

    def posIncrement(self , step = 1):
        self.currPos = self.currPos + step

    def skipWhiteSpace(self):
        while (self.endOfFile() == False and self.currChar() == " "):
            self.posIncrement()
    def findNext(self,findC,startPos):
        for i in range(startPos , self.length):
            if i == findC:
                return i
        return None

    def endOfFile(self):
        if self.currPos >= len(self.input):
            return True
        else:
            return False
    def currSubstring(self , Length):
        Length = min(Length , self.length)
        start = self.currPos
        end = self.currPos + Length
        return self.input[start : end]
    
    def getLexeme(self):
        lexeme = []
        while self.endOfFile() == False:
    
            if self.currChar() == " ":
                self.skipWhiteSpace()
            
            elif self.currSubstring(5) == "PRINT":
                lexeme.append(TokenType.PRINT)
                self.posIncrement(step = 5)
            elif self.currSubstring(4) == "GOTO":
                lexeme.append(TokenType.GOTO)
                self.posIncrement(step = 4)
            elif self.currSubstring(5) == "LABEL":
                lexeme.append(TokenType.LABEL)
                self.posIncrement(step = 5)
            elif self.currSubstring(5) == "INPUT":
                lexeme.append(TokenType.INPUT)
                self.posIncrement(step = 5)
            elif self.currSubstring(3) == "LET":
                lexeme.append(TokenType.LET)
                self.posIncrement(step = 3)
            elif self.currSubstring(2) == "IF":
                lexeme.append(TokenType.IF)
                self.posIncrement(step = 2)
            elif self.currSubstring(5) == "LABEL":
                lexeme.append(TokenType.LABEL)
                self.posIncrement(step = 5)
            elif self.currSubstring(4) == "THEN":
                lexeme.append(TokenType.THEN)
                self.posIncrement(step = 4)
            elif self.currSubstring(5) == "ENDIF":
                lexeme.append(TokenType.ENDIF)
                self.posIncrement(step = 5)
            elif self.currSubstring(5) == "WHILE":
                lexeme.append(TokenType.WHILE)
                self.posIncrement(step = 5)
            elif self.currSubstring(6) == "REPEAT":
                lexeme.append(TokenType.REPEAT)
                self.posIncrement(step = 6)
            elif self.currSubstring(5) == "ENDWHILE":
                lexeme.append(TokenType.ENDWHILE)
                self.posIncrement(step = 5)
            elif self.currSubstring(2) == "==":
                lexeme.append(TokenType.EQEQ)
                self.posIncrement(step = 2)
            elif self.currSubstring(2) == ">=":
                lexeme.append(TokenType.GTEQ)
                self.posIncrement(step = 2)
            elif self.currSubstring(2) == "<=":
                lexeme.append(TokenType.LTEQ)
                self.posIncrement(step = 2)
            
            elif self.currChar() == "+":
                lexeme.append(TokenType.PLUS)
                self.posIncrement()
            elif self.currChar() == "-":
                lexeme.append(TokenType.MINUS)
                self.posIncrement()
            elif self.currChar() == "*":
                lexeme.append(TokenType.ASTERISK)
                self.posIncrement()
            elif self.currChar() == "/":
                lexeme.append(TokenType.SLASH)
                self.posIncrement()
            elif self.currChar() == "=":
                lexeme.append(TokenType.EQ)
                self.posIncrement()
            elif self.currChar() == ">":
                lexeme.append(TokenType.GT)
                self.posIncrement()
            elif self.currChar() == "<":
                lexeme.append(TokenType.LT)
                self.posIncrement()
            


        return lexeme


def main():
    lex = lexer("+-* == REPEAT")
    print(lex.getLexeme())

main()




# TokenType is our enum for all the types of tokens.

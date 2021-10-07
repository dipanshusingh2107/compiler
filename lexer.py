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
            if self.input[i] == findC:
                return i
        return None
        
    def getIdentifierEnd(self):
        pos = self.currPos-1
        if not self.currChar().isalpha():
            return None

        while(pos < self.length):
            if self.input[pos+1].isalnum():
                pos = pos+1
            else:
                return pos
            

        return min(pos,self.length-1)

    

    def getNumberEnd(self):
        pos = self.currPos -1
        if not self.currChar().isdigit():
            return None

        while pos < self.length:
            if self.input[pos+1].isdigit():
                pos = pos+1
            else:
                return pos
            

        return min(pos,self.length-1)

    

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
            elif self.currChar() == "\"":
                pos = self.findNext("\"" , self.currPos+1)
                if pos != None:
                    lexeme.append(TokenType.STRING)
                    self.posIncrement(step = pos-self.currPos+1)
                else:
                    lexeme.append("ERROR")
                    break
            
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

            elif self.currChar().isalpha():
                pos = self.getIdentifierEnd()
                lexeme.append(TokenType.IDENT)
                self.posIncrement(step = pos-self.currPos+1)

            elif self.currChar().isdigit():
                pos = self.getNumberEnd()
                lexeme.append(TokenType.NUMBER)
                self.posIncrement(step = pos-self.currPos+1)


        return lexeme


def main():
    lex = lexer("123apple34+-* == REPEAT \"hellloo ")
    for i in lex.getLexeme():
        print(i)

main()




# TokenType is our enum for all the types of tokens.

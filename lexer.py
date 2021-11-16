from tokens import TokenType
class Lexer():
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

        while(pos+1 < self.length):
            if self.input[pos+1].isalnum() and self.keywordStart(pos+1) == False:
                pos = pos+1
            else:
                return pos
    
            

        return min(pos,self.length-1)

    

    def getNumberEnd(self):
        pos = self.currPos -1
        if not self.currChar().isdigit():
            return None

        while pos < self.length-1:
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
    def getSubstring(self,start , end):
        start = max(start,0)
        start = min(start , self.length)
        end = max(end,0)
        end = min(end , self.length)
        return self.input[start:end]

    def isKeyword(self,keyword):
        if keyword == "PRINT":
            return TokenType.PRINT
        elif keyword == "GOTO":
            return TokenType.GOTO
        elif keyword == "LABEL":
            return TokenType.LABEL
        elif keyword == "INPUT":
            return TokenType.INPUT
        elif keyword == "LET":
            return TokenType.LET  
        elif keyword == "IF":
            return TokenType.IF
        elif keyword == "THEN":
            return TokenType.THEN
        elif keyword == "ENDIF":
            return TokenType.ENDIF
        elif keyword == "WHILE":
            return TokenType.WHILE
        elif keyword == "REPEAT":
            return TokenType.REPEAT
        elif keyword == "ENDWHILE":
            return TokenType.ENDWHILE
        return None
        
    def keywordStart(self,pos):
        for i in range(0,9):
            s = self.getSubstring(pos , pos+i)
            if self.isKeyword(s):
                return True
        return False

    def getLexeme(self):
        lexeme = []
        text = []
        while self.endOfFile() == False:
    
            if self.currChar() == " ":
                self.skipWhiteSpace()
            if self.currChar() == "\n":
                lexeme.append(TokenType.NEWLINE)
                text.append("\n")
                self.posIncrement()
            elif self.currChar() == "\"":
                pos = self.findNext("\"" , self.currPos+1)
                if pos != None:
                    lexeme.append(TokenType.STRING)
                    text.append(self.getSubstring(self.currPos , pos+1))
                    self.posIncrement(step = pos-self.currPos+1)
                else:
                    lexeme.append("ERROR")
                    text.append("ERROR")
                    break
            
            elif self.currSubstring(5) == "PRINT":
                lexeme.append(TokenType.PRINT)
                text.append("PRINT")
                self.posIncrement(step = 5)
            elif self.currSubstring(4) == "GOTO":
                text.append("GOTO")
                lexeme.append(TokenType.GOTO)
                self.posIncrement(step = 4)
            elif self.currSubstring(5) == "LABEL":
                text.append("LABEL")
                lexeme.append(TokenType.LABEL)
                self.posIncrement(step = 5)
            elif self.currSubstring(5) == "INPUT":
                text.append("INPUT")
                lexeme.append(TokenType.INPUT)
                self.posIncrement(step = 5)
            elif self.currSubstring(3) == "LET":
                lexeme.append(TokenType.LET)
                text.append("LET")
                self.posIncrement(step = 3)
            elif self.currSubstring(2) == "IF":
                lexeme.append(TokenType.IF)
                text.append("IF")
                self.posIncrement(step = 2)
            elif self.currSubstring(4) == "THEN":
                lexeme.append(TokenType.THEN)
                text.append("THEN")
                self.posIncrement(step = 4)
            elif self.currSubstring(5) == "ENDIF":
                lexeme.append(TokenType.ENDIF)
                text.append("ENDIF")
                self.posIncrement(step = 5)
            elif self.currSubstring(5) == "WHILE":
                lexeme.append(TokenType.WHILE)
                text.append("WHILE")
                self.posIncrement(step = 5)
            elif self.currSubstring(6) == "REPEAT":
                lexeme.append(TokenType.REPEAT)
                text.append("REPEAT")
                self.posIncrement(step = 6)
            elif self.currSubstring(8) == "ENDWHILE":
                lexeme.append(TokenType.ENDWHILE)
                text.append("ENDWHILE")
                self.posIncrement(step = 8)
        
            elif self.currSubstring(2) == "==":
                lexeme.append(TokenType.EQEQ)
                text.append("==")
                self.posIncrement(step = 2)
            elif self.currSubstring(2) == ">=":
                lexeme.append(TokenType.GTEQ)
                text.append(">=")
                self.posIncrement(step = 2)
            elif self.currSubstring(2) == "<=":
                lexeme.append(TokenType.LTEQ)
                text.append("<=")
                self.posIncrement(step = 2)
            
            elif self.currChar() == "+":
                lexeme.append(TokenType.PLUS)
                text.append("+")
                self.posIncrement()
            elif self.currChar() == "-":
                lexeme.append(TokenType.MINUS)
                text.append("-")
                self.posIncrement()
            elif self.currChar() == "*":
                lexeme.append(TokenType.ASTERISK)
                text.append("*")
                self.posIncrement()
            elif self.currChar() == "/":
                lexeme.append(TokenType.SLASH)
                text.append("/")
                self.posIncrement()
            elif self.currChar() == "=":
                lexeme.append(TokenType.EQ)
                text.append("=")
                self.posIncrement()
            elif self.currChar() == ">":
                lexeme.append(TokenType.GT)
                text.append(">")
                self.posIncrement()
            elif self.currChar() == "<":
                lexeme.append(TokenType.LT)
                text.append("<")
                self.posIncrement()

            elif self.currChar().isalpha():
                pos = self.getIdentifierEnd()
                lexeme.append(TokenType.IDENT)
                text.append(self.getSubstring(self.currPos , pos+1))
                self.posIncrement(step = pos-self.currPos+1)

            elif self.currChar().isdigit():
                pos = self.getNumberEnd()
                lexeme.append(TokenType.NUMBER)
                text.append(self.getSubstring(self.currPos , pos+1))
                self.posIncrement(step = pos-self.currPos+1)
            else:
                lexeme.append("ERROR")
                text.append("ERROR")
                break


        return lexeme , text


def main():

    file = open('test.sv')
    data = ""
    data = file.read()
    data+= '\n'

    lex = Lexer(data)
    for i in lex.getLexeme():
        print(i)

if __name__ == "__main__":
    main()




# TokenType is our enum for all the types of tokens.

from tokens import TokenType

class parser():
    def __init__(self , token) :
        self.token = token
        self.currTokenPos = 0
        self.numberOfTokens = len(token)
    
    def increasePos(self , step = 1):
        self.currTokenPos+=step
    
    def currToken(self):
        return self.token[self.currTokenPos]

    def program(self):
        print("Program Parsing begins!")
        while(self.currTokenPos < self.numberOfTokens):
            self.statements()
    
    def nl(self):
        while(self.currToken == TokenType.NEWLINE):
            self.increasePos()

    def statements(self):
        pass
class parser():
    def __init__(self , token) :
        self.token = token
        self.currTokenPos = 0
        self.numberOfTokens = len(token)
    
    def currToken(self):
        return self.token[self.currTokenPos]

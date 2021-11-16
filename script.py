from lexer import Lexer
from tokens import TokenType
from parser import Parser
import sys , os

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


def main():
    file = open('test.sv' , "r")
    data = file.read()
    file.close()
    data += '\n'

    lexer = Lexer(data) #lexer declared

    lexeme , text = lexer.getLexeme()  #token taken

    if "ERROR" in lexeme:
        sys.exit("Lexer ERROR")
    
    if len(lexeme) != len(text):
        sys.exit("Error len(Lexer) != len(Text)")
    
    lexeme.append(TokenType.EOF)
    text.append("EOF")
    
    # for token in lexeme:
    #     print(token)

    parser = Parser(lexeme , text) 

    blockPrint()    #used to supress the output from the parser
    parser.program()    #parsed
    enablePrint()   #use to enable the print

    file = open("output.py" , "w");
    file.write(parser.out)
    file.close()

    os.system("python3 output.py")

    
main()

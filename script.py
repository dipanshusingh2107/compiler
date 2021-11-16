from lexer import Lexer
from tokens import TokenType
from parser import Parser




def main():
    file = open('test.sv' , "r")
    data = file.read()
    file.close()
    data += '\n'

    lexer = Lexer(data) #lexer declared

    lexeme , text = lexer.getLexeme()  #token taken

    if "ERROR" in lexeme:
        print("Lexer ERROR")
    
    if len(lexeme) != len(text):
        print("ERROR LEXEME != TEXT")
    
    print(text)
    lexeme.append(TokenType.EOF)
    
    # for token in lexeme:
    #     print(token)

    parser = Parser(lexeme , text) 
    parser.program()    #parsed

    file = open("output.py" , "w");
    file.write(parser.out)
    file.close()

main()

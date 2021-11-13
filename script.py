from lexer import Lexer
from tokens import TokenType
from parser import Parser




def main():
    file = open('test.tiny')
    data = file.read()
    data += '\n'

    lexer = Lexer(data)

    lexeme = lexer.getLexeme()
    lexeme.append(TokenType.EOF)
    
    for token in lexeme:
        print(token)

    parser = Parser(lexeme)
    parser.program()

main()

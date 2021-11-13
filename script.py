from lexer import Lexer
from tokens import TokenType
from parser import Parser




def main():
    file = open('test.tiny')
    data = file.read()
    data += '\n'

    lexer = Lexer(data)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()

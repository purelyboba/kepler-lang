from lang import error, lexer, position, token, nodes, parser

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndex = -1
        self.advance()
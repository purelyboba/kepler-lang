from lang import error, lexer, position, token, nodes, parser

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndex = -1
        self.advance()

    def advance(self):
        self.tokenIndex += 1
        if self.tokenIndex < len(self.tokens):
            self.currentToken = self.tokens[self.tokenIndex]

    # return abstract syntax tree
    def parse(self):
        return self.tokens
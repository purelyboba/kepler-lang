from lang import error, lexer, position, token, nodes, parser

TT_INT		= 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'

DIGITS = '0123456789'

class Lexer:
    def __init__(self, fileName, text):
        self.fileName = fileName
        self.text = text
        self.pos = position.Position(-1, 0, -1, fileName, text)
        self.currentChar = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.currentChar)
        self.currentChar = self.text[self.pos.index] if self.pos.index < len(self.text) else None

    def makeTokens(self):
        tokens = []

        while self.currentChar != None:
            if self.currentChar in ' \t':
                self.advance()
            elif self.currentChar in DIGITS:
                tokens.append(self.makeNumber())
            elif self.currentChar == '+':
                tokens.append(token.Token(TT_PLUS))
                self.advance()
            elif self.currentChar == '-':
                tokens.append(token.Token(TT_MINUS))
                self.advance()
            elif self.currentChar == '*':
                tokens.append(token.Token(TT_MUL))
                self.advance()
            elif self.currentChar == '/':
                tokens.append(token.Token(TT_DIV))
                self.advance()
            elif self.currentChar == '(':
                tokens.append(token.Token(TT_LPAREN))
                self.advance()
            elif self.currentChar == ')':
                tokens.append(token.Token(TT_RPAREN))
                self.advance()
            else:
                posStart = self.pos.copy()
                char = self.currentChar
                self.advance()
                return [], error.IllegalCharError(posStart, self.pos, "'" + char + "'")

        return tokens, None

    def makeNumber(self):
        numStr = ''
        dotCount = 0

        while self.currentChar != None and self.currentChar in DIGITS + '.':
            if self.currentChar == '.':
                if dotCount == 1: break
                dotCount += 1
                numStr += '.'
            else:
                numStr += self.currentChar
            self.advance()

        if dotCount == 0:
            return token.Token(TT_INT, int(numStr))
        else:
            return token.Token(TT_FLOAT, float(numStr))
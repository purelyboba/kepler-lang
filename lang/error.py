from lang import error, lexer, position, token, nodes, parser

class Error:
    def __init__(self, posStart, posEnd, errorName, details):
        self.posStart = posStart
        self.posEnd = posEnd
        self.errorName = errorName
        self.details = details
    
    def as_string(self):
        result  = f'{self.errorName}: {self.details}\n'
        result += f'File {self.posStart.fileName}, line {self.posStart.lineNumber + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, posStart, posEnd, details):
        super().__init__(posStart, posEnd, 'Illegal Character', details)
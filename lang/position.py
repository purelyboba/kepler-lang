from lang import error, lexer, position, token, nodes, parser

class Position:
    def __init__(self, index, lineNumber, column, fileName, text):
        self.index = index
        self.lineNumber = lineNumber
        self.column = column
        self.fileName = fileName
        self.text = text

    def advance(self, currentChar):
        self.index += 1
        self.column += 1

        if currentChar == '\n':
            self.lineNumber += 1
            self.column = 0

        return self

    def copy(self):
        return Position(self.index, self.lineNumber, self.column, self.fileName, self.text)
from lang import error, lexer, position, token, nodes

def run(fileName, text):
    l = lexer.Lexer(fileName, text)
    tokens, error = l.makeTokens()

    return tokens, error
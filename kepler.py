from lang import error, lexer, position, token, nodes, parser

def run(fileName, text):
    l = lexer.Lexer(fileName, text)
    tokens, error = l.makeTokens()

    p = parser.Parser(tokens)
    ast = p.parse()

    return ast, error
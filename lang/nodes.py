from lang import error, lexer, position, token, nodes, parser

class NumberNode:
    def __init__(self, token):
        self.token = token
    
    def __repr__(self):
        return f'{self.token}'

class BinaryOperationNode:
    def __init__(self, leftNode, operatorToken, rightNode):
        self.leftNode = leftNode
        self.operatorToken = operatorToken
        self.rightNode = rightNode

    def __repr__(self):
        return f'({self.leftNode}, {self.operatorToken}, {self.rightNode})'

class UnaryOperationNode:
    def __init__(self, operatorToken, node):
        self.operatorToken = operatorToken
        self.node = node

    def __repr__(self):
        return f'({self.operatorToken}, {self.node})'
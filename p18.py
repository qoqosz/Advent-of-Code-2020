# Part 1
from collections import namedtuple

Token = namedtuple('Token', 'type value')
TOKENS = {'+': 'PLUS', '*': 'MUL', '(': 'LPAREN', ')': 'RPAREN'}


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        res = ''

        while self.current_char is not None and self.current_char.isdigit():
            res += self.current_char
            self.advance()

        return int(res)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token('INT', self.integer())

            if self.current_char in TOKENS:
                c = self.current_char
                self.advance()
                return Token(TOKENS[c], c)

            raise ValueError('Error, unknown char')

        return Token('EOF', None)


class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            print(self.current_token)
            raise ValueError('Invalid syntax')

    def factor(self):
        token = self.current_token

        if token.type == 'INT':
            self.eat('INT')
            return token.value
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            res = self.term()
            self.eat('RPAREN')
            return res

    def term(self):
        res = self.factor()

        while self.current_token.type in ('PLUS', 'MUL'):
            token = self.current_token

            if token.type == 'PLUS':
                self.eat('PLUS')
                res += self.factor()
            elif token.type == 'MUL':
                self.eat('MUL')
                res *= self.factor()

        return res


with open('p18.txt') as f:
    print(sum(Interpreter(Lexer(line.strip())).term()
              for line in f))


# Part 2
class InterpreterP2(Interpreter):
    def factor(self):
        token = self.current_token

        if token.type == 'INT':
            self.eat('INT')
            return token.value
        elif token.type == 'LPAREN':
            self.eat('LPAREN')
            res = self.expr()
            self.eat('RPAREN')
            return res

    def term(self):
        res = self.factor()

        while self.current_token.type == 'PLUS':
            token = self.current_token

            if token.type == 'PLUS':
                self.eat('PLUS')
                res += self.factor()

        return res

    def expr(self):
        res = self.term()

        while self.current_token.type == 'MUL':
            token = self.current_token

            if token.type == 'MUL':
                self.eat('MUL')
                res *= self.term()

        return res


with open('p18.txt') as f:
    print(sum(InterpreterP2(Lexer(line.strip())).expr()
              for line in f))

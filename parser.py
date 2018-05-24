main.py
parser.py
indent.py
lexer.py
token.pyimport sys
from indent import Indent
from ast import AST


class Parser:

    TYPE = ['INT', 'FLOAT', 'CHAR']
    STATEMENT_STARTERS = ['SEMICOLON', 'LBRACE', 'IDENTIFIER', 'IF', 'WHILE']
    REL_OP = ['LT', 'LTE', 'GT', 'GTE','EQ']
    MUL_OP = ['MUL', 'DIV']
    ASSIGN_OP = ['ASSIGN']
    LITERAL = ['INTEGER_LIT', 'FLOAT_LIT', 'CHAR_LIT']

    def __init__(self, verbose=False):
        self.indentator = Indent(verbose)
        self.tokens = []
        self.errors = 0

    def show_next(self, n=1):
        try:
            return self.tokens[n - 1]
        except IndexError:
            print('ERROR: no more tokens left!')
            sys.exit(1)

    def expect(self, kind):
        actualToken = self.show_next()
        actualKind = actualToken.kind
        actualPosition = actualToken.position
        if actualKind == kind:
            return self.accept_it()
        else:
            print('Error at {}: expected {}, got {} instead'.format(str(actualPosition), kind, actualKind))
            sys.exit(1)

    # same as expect() but no error if not correct kind
    def maybe(self, kind):
        if self.show_next().kind == kind:
            return self.accept_it()

    def accept_it(self):
        token = self.show_next()
        output = str(token.kind) + ' ' + token.value
        self.indentator.say(output)
        return self.tokens.pop(0)

    def remove_comments(self):
        result = []
        in_comment = False
        for token in self.tokens:
            if token.kind == 'COMMENT':
                pass
            elif token.kind == 'LCOMMENT':
                in_comment = True
            elif token.kind == 'RCOMMENT':
                in_comment = False
            else:
                if not in_comment:
                    result.append(token)
        return result

    def parse(self, tokens):
        self.tokens = tokens
        self.tokens = self.remove_comments()
        self.parse_program()

    def parse_program(self):
        #print(self.tokens)
        self.indentator.indent('Parsing Program')
        self.expect('INT')
        self.expect('IDENTIFIER')
        self.expect('LPAREN')
        self.expect('RPAREN')
        self.expect('LBRACE')

        self.parse_declarations()
        self.parse_statements()

        self.expect('RBRACE')
        self.indentator.dedent()
        if (self.errors == 1):
            print('WARNING: 1 error found!')
        elif (self.errors > 1):
            print('WARNING: ' + str(self.errors) + ' errors found!')
        else:
            print('parser: syntax analysis successful!')

    def parse_declarations(self):
        self.indentator.indent('Parsing Declarations')
        
        while self.show_next().kind in self.TYPE :

            self.parse_declaration()

        
        self.indentator.dedent()


    def parse_declaration(self):
        self.indentator.indent('Parsing Declaration')

        if self.show_next().kind in self.TYPE :

            self.accept_it()
            dec = Declaration()
            
        self.expect('IDENTIFIER')
        
        if self.show_next().kind == 'LBRACKET' :

            self.expect('LBRACKET')
            self.expect('INTEGER_LIT')
            self.expect('RBRACKET')

        while self.show_next().kind == 'COMMA':
            
            self.expect('COMMA')
            self.expect('IDENTIFIER')
            
            if self.show_next().kind == 'LBRACKET' :
                
                self.expect('LBRACKET')
                self.expect('INTEGER_LIT')
                self.expect('RBRACKET')

        self.expect('SEMICOLON')
        
        self.indentator.dedent()

        return()

        
    def parse_statements(self):
        self.indentator.indent('Parsing Statements')
        
        while self.show_next().kind in self.STATEMENT_STARTERS :
           
            self.parse_statement()

        self.indentator.dedent()

    def parse_statement(self):
        self.indentator.indent('Parsing Statements')
        
        if self.show_next().kind == 'IF':
            self.parse_if()
        if self.show_next().kind == 'WHILE':
            self.parse_statementwhile()
        if self.show_next().kind == 'LBRACE':
            self.parse_block()
        if self.show_next().kind == 'SEMICOLON':
            self.accept_it()
        if self.show_next().kind == 'IDENTIFIER'
            self.parse_assignement()

        self.indentator.dedent()

    def parse_if(self): #DONE

        self.indentator.indent('Parsing Declaration')
        self.expect('LPAREN')
        self.parse_expression()
        self.expect('RPAREN')
        self.parse_statement()

        if show_next().kind == 'ELSE':
            self.accept_it()
            self.parse_statement()

        self.indentator.dedent()

    def parse_expression(self):

        self.indentator.indent('Parsing Expression')

    def parse_assignement(self):

        self.indentator.indent('Parsing Assignement')
        self.expect('IDENTIFIER')

        self.expect('ASSIGN')

        self.parse_expression()
        self.expect('SEMICOLON')



    def parse_block(self): #DONE
        self.indentator.indent('Parsing Block')
        self.expect('LBRACE')
        self.parse_statements()
        self.expect('RBRACE')

        self.indetator.dedent()





#def parse_statementwhile(self):

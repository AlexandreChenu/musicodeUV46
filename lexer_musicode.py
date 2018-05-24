import re
import sys
from token import Token


regexExpressions = [

	(r'for\b', 'FOR'),
    (r'if\b', 'IF'),
    (r'else\b', 'ELSE'),
    (r'while\b', 'WHILE'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\[', 'LBRACKET'),
    (r'\]', 'RBRACKET'),
    (r'\;', 'SEMICOLON'),
    (r'\:', 'COLON'),
    (r'\,', 'COMMA'),
    (r'\/\*', 'LCOMMENT'),
    (r'\*\/', 'RCOMMENT'),
    (r'\/\/(.*)', 'COMMENT'),

    #propre à musicode

    (r'play\b', 'PLAY')
    (r'hand_declare\b', 'HAND_D')
    (r'def\b','DEF')
    
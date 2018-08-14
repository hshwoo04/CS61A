#  Name: Sung Hyun Woo  
#  Email: shwoo@berkeley.edu


# A dictionary from pairs of matching brackets to the operators they indicate.
BRACKETS = {('[', ']'): '+',
            ('(', ')'): '-',
            ('<', '>'): '*',
            ('{', '}'): '/'}

# A dictionary with left-bracket keys and corresponding right-bracket values.
LEFT_RIGHT = {left:right for left, right in BRACKETS.keys()}

# The set of all left and right brackets.
ALL_BRACKETS = set(b for bs in BRACKETS for b in bs)

# Q1.

def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('2.3')
    [2.3]
    >>> tokenize('(2 3)')
    ['(', 2, 3, ')']
    >>> tokenize('<2 3)')
    ['<', 2, 3, ')']
    >>> tokenize('<[2{12.5 6.0}](3 -4 5)>')
    ['<', '[', 2, '{', 12.5, 6.0, '}', ']', '(', 3, -4, 5, ')', '>']

    >>> tokenize('2.3.4')
    Traceback (most recent call last):
        ...
    ValueError: invalid token 2.3.4

    >>> tokenize('?')
    Traceback (most recent call last):
        ...
    ValueError: invalid token ?

    >>> tokenize('hello')
    Traceback (most recent call last):
        ...
    ValueError: invalid token hello

    >>> tokenize('<(GO BEARS)>')
    Traceback (most recent call last):
        ...
    ValueError: invalid token GO
    """
    # Surround all brackets by spaces so that they are separated by split.
    for b in ALL_BRACKETS:
        line = line.replace(b, ' ' + b + ' ')

    # Convert numerals to numbers and raise ValueErrors for invalid tokens.
    tokens = []
    comp_list = []
    for a in line.split(' '):
        if a!= ' ':
            comp_list.append(a)
    for x in comp_list:
        if a in ALL_BRACKETS:
            token.append(a)
    else:
        num = coerce_to_number(a)
        if num == None:
            raise ValueError
        else:
            token.append(num)
    return tokens

def coerce_to_number(token):
    """Coerce a string to a number or return None.

    >>> coerce_to_number('-2.3')
    -2.3
    >>> print(coerce_to_number('('))
    None
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return None

# Q2.

def brack_read(tokens):
    """Return an expression tree for the first well-formed Brackulator
    expression in tokens. Tokens in that expression are removed from tokens as
    a side effect.

    >>> brack_read(tokenize('100'))
    100
    >>> brack_read(tokenize('([])'))
    Pair('-', Pair(Pair('+', nil), nil))
    >>> print(brack_read(tokenize('<[2{12 6}](3 4 5)>')))
    (* (+ 2 (/ 12 6)) (- 3 4 5))
    >>> brack_read(tokenize('(1)(1)')) # More than one expression is ok
    Pair('-', Pair(1, nil))
    >>> brack_read(tokenize('[])')) # Junk after a valid expression is ok
    Pair('+', nil)

    >>> brack_read(tokenize('([]')) # Missing right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line

    >>> brack_read(tokenize('[)]')) # Extra right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )

    >>> brack_read(tokenize('([)]')) # Improper nesting
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )

    >>> brack_read(tokenize('')) # No expression
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line
    """
    if not tokens:
        raise SyntaxError('unexpected end of line')
    token = tokens.pop(0)
    n = coerce_to_number(token)
    if n != None:
        return n
    elif token in LEFT_RIGHT:
        m = LEFT_RIGHT(n)

    def read_tail(tokens):
        num = tokens.pop(0)
        if num in [')','>',']','}']:
            return (num,brack_read(tokens))
        else:
            return nil


    def make_pair(ex_list):
        if  ex_list ==[]:
            return nil
        else:
            return Pair(ex_list[0], make_pair(ex_list[1:]))

    def helper(tokens):
        if tokens==[]:
            return ValueError
        num = tokens.pop(0)
        line = []
        if LEFT_RIGHT[num] in tokens:
            for x in tokens:
                if tokens[x] != LEFT_RIGHT[num]:
                    line.append(x)
            line.append(LEFT_RIGHT(num))

    return helper(tokens)


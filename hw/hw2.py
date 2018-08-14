#  Name:
#  Email:


def square(x):
    """Return x squared."""
    return x * x

# Q1.

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    sum=1
    while n>0:
      sum=sum*term(n)
      n-=1
    return sum


def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    """
    def one(x):
      return x
    return product(n,one)



# Q2.

def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    return combiner(n)



def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """

    def combiner(n):
        if n==1:
            return term(n)
        else:
            return term(n)+combiner(n-1)

    return accumulate(combiner, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    def combiner(n):
        if n==1:
            return term(n)
        else:
            return term(n)*combiner(n-1)

    return accumulate(combiner, 0, n, term)



# Q3.

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    def compose1(f,g):
        def h(x):
            return f(g(x))
        return h
    return compose1(f,f)


# Q4.

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """

    def helper(number):
        if n==1:
            return f(number)
        else:
            return f(repeated(f,n-1)(number))
    return helper

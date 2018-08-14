#  Name:Sung Hyun Woo
#  Email: shwoo@berkeley.edu

# Q1.

def overlaps(low0, high0, low1, high1):
    """Return whether the open intervals (LOW0, HIGH0) and (LOW1, HIGH1)
    overlap.

    >>> overlaps(10, 15, 14, 16)
    True
    >>> overlaps(10, 15, 1, 5)
    False
    >>> overlaps(10, 10, 9, 11)
    False
    >>> result = overlaps(1, 5, 0, 3)  # Return, don't print
    >>> result
    True
    """
    if low0==high0 or high0==high1:
        return False
    elif low0<=low1<high0:
        return True
    elif low0<high1<=high0:
        return True
    elif low1<=low0<high1:    
        return True
    elif low1<high0<=high1:
        return True
    else:
        return False



# Q2.
from math import sqrt
def last_square(x):
    """Return the largest perfect square less than X, where X>0.

    >>> last_square(10)
    9
    >>> last_square(39)
    36
    >>> last_square(100)
    81
    >>> result = last_square(2) # Return, don't print
    >>> result
    1
    """
    def square(x):
        return x*x
    if sqrt(x)%1==0:
        n=square(sqrt(x)-1)
    else:
        n=square(sqrt(x)//1)
    return int(n)



# Q3.

def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
   
    while x > 0:
        ones = x%10
        tens = (x//10)%10
        if ones < tens:
            return False
        x = x//10
    return True






    

#  Name: Sung Hyun Woo
#  Email: shwoo@berkeley.edu

# Q1.

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n<=3:
        return n
    else:
        return g(n-1)+(2*g(n-2))+(3*g(n-3))

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """

    if n<=3:
        return n
    x=1
    y=2
    z=3
    i=4
    while i<=n:
        x, y, z=y, z, (3*x+2*y+z)
        i+=1
    return z


# Q2.

def has_seven(k):
    """Has a has_seven
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k%10==7:
        return True
    elif k<10:
        return False
    else:
        return has_seven(k//10)

# Q3.

"1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6"


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    def helper(num, value, direction):

        if num==n+1:
            return value
        elif num%7==0 or has_seven(num)==True:
            if direction==True:
                return helper(num+1, value+1, False)
            if direction==False:
                return helper(num+1, value-1, True)
        else:
            if direction==True:
                return helper(num+1, value+1, True)
            elif direction==False:
                return helper(num+1, value-1, False)

    return helper(1,0,True)

    # Q4.

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    

    def helper(n,num=0,last_digit=n%10): 
        if n==0:
            return num
        elif ((n//10)%10)+last_digit==10:
            num+=1
            return helper(n//10,num,last_digit)
        else:
            return helper(n//10,num,last_digit)
    
    if n==0:
        return 0
    else:
        return helper(n,0, n%10)+ten_pairs(n//10)



# Q5.

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def helper(amount):
        if amount=0
            return 0
        elif (amount/2)%2==0:
            return  helper(amount/2)
        else:
            return helper(amount/2)
    if amount==0:
        return 0
    return count_change(amount)+helper(n/2)


   










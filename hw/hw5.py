#  Name: Sung Hyun Woo      
#  Email: shwoo@berkeley.edu

# Q1.

def reverse_list(s):
    """Reverse the contents of list s and return None.

    >>> digits = [6, 2, 9, 5, 1, 4, 1, 3]
    >>> reverse_list(digits)
    >>> digits
    [3, 1, 4, 1, 5, 9, 2, 6]
    >>> d = digits
    >>> reverse_list(d)
    >>> digits
    [6, 2, 9, 5, 1, 4, 1, 3]
    """
    k=len(s)-1
    while k>=0:
        s.append(s[k])
        k-=1    
    num=0
    while num<len(s):
        del s[0]
        num+=1 
    return None

# Q2.

def card(n):
    """Return the playing card type for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> suits = ['â™¡', 'â™¢', 'â™¤', 'â™§']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['Aâ™¡', 'Aâ™¢', 'Aâ™¤', 'Aâ™§', '2â™¡', '2â™¢', '2â™¤', '2â™§', '3â™¡', '3â™¢', '3â™¤', '3â™§']
    >>> cards[26:30]
    ['7â™¤', '7â™§', '8â™¡', '8â™¢']
    >>> shuffle(cards)[:12]
    ['Aâ™¡', '7â™¤', 'Aâ™¢', '7â™§', 'Aâ™¤', '8â™¡', 'Aâ™§', '8â™¢', '2â™¡', '8â™¤', '2â™¢', '8â™§']
    >>> shuffle(shuffle(cards))[:12]
    ['Aâ™¡', '4â™¢', '7â™¤', '10â™§', 'Aâ™¢', '4â™¤', '7â™§', 'Jâ™¡', 'Aâ™¤', '4â™§', '8â™¡', 'Jâ™¢']
    >>> cards[:12]  # Should not be changed
    ['Aâ™¡', 'Aâ™¢', 'Aâ™¤', 'Aâ™§', '2â™¡', '2â™¢', '2â™¤', '2â™§', '3â™¡', '3â™¢', '3â™¤', '3â™§']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    half=len(cards)//2
    n=0
    first_half=[]
    second_half=[]
    while n<=half:
        first_half.append(cards[n])
        n+=1
    n=half
    while n<=len(cards)-1:
        second_half.append(cards[n])
        n+=1
    k=0
    new_list=[]
    while k<(max(len(first_half), len(second_half))-1):
        new_list.append(first_half[k])
        new_list.append(second_half[k])
        k+=1
    return new_list

# Q3.

G = { 'A': ['B', 'D'], 'B': ['C'], 'C': ['F'], 'D': ['E'], 
      'E': ['F'], 'F': ['G'], 'G': ['A'] }


def is_circular(G):
    """Return true iff G represents a circular directed graph."""
    for v in G:
        if reaches_circularity(G, v):
            return True
    return False

def reaches_circularity(G, v0):
    """Returns true if there is a circularity in G in some path
    starting from vertex V0."""
    def is_path_to_cycle(v1):
        for w in G[v1]:
            if v0 == w:
                return True
            if is_path_to_cycle(w):
                return True
        return False
    return is_path_to_cycle(v0)


def reaches_circularity(G, v0):
    """Returns true if there is a circularity in G in some path
    starting from vertex V0.
    >>> G = { 'A': ['B', 'D'], 'B': ['C'], 'C': ['F'], 'D': ['E'], 
    ...       'E': ['F'], 'F': ['G'], 'G': ['A'] }
    >>> is_circular(G)
    True
    >>> G['F'] = []
    >>> is_circular(G)
    False
    """
    def is_path_to_cycle(v1):
        for w in G[v1]:
            k=1
            if k>len(list(G)):
                return False
            if v0==w:
                return True
            else:
                k+=1
                return is_path_to_cycle(w)
    return is_path_to_cycle(v0)




# Q4.

def make_withdraw(balance):
    """Return a withdraw function with BALANCE as its starting balance.
    >>> withdraw = make_withdraw(1000)
    >>> withdraw(100)
    900
    >>> withdraw(100)
    800
    >>> withdraw(900)
    'Insufficient funds'
    """
    
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
           return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    incorrect_list=[]
    def withdraw_function(amount, password_attempt):
        if len(incorrect_list)>=3:
           return "Your account is locked. Attempts: %s" %incorrect_list 
        if password_attempt!=password:
            incorrect_list.append(password_attempt)
            return 'Incorrect password'
        elif password_attempt==password:
            nonlocal balance
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
 
    return withdraw_function





# Q5.

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    


    def joint_withdraw_function(amount, joint_password_attempt):
        if joint_password_attempt==old_password or joint_password_attempt==new_password:
            return withdraw(amount, old_password)
        else:
            return withdraw(amount, joint_password_attempt)
            

    a= withdraw(0,old_password)
    if type(a)==str: #how to check if old password is correct?
        return a
    elif type(a)!=str:
        return joint_withdraw_function



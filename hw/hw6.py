#  Name: Sung Hyun Woo  
#  Email: shwoo@berkeley.edu

# Q0.
# Q1.

class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    stock=0
    amount=0
    def __init__(self, name, price):
        self.name=name
        self.price=price

    def restock(self,num):
        self.stock+=num
        return 'Current %s stock: %i' %(self.name, self.stock)


    def deposit(self, amount):
        self.amount+=amount
        if self.stock==0:
            previous_amount=self.amount
            self.amount==0
            return 'Machine is out of stock. Here is your $%i.' %(previous_amount)
        return 'Current balance: $%i' %(self.amount)


    def vend(self):
        if self.stock==0:
            if self.amount<self.price:
                return 'Machine is out of stock.'
            else:
                previous_amount=self.amount
                self.amount=0
                return 'Machine is out of stock. Here is your $%i.' %(previous_amount)
        if self.amount<self.price:
            return 'You must deposit $%i more.' %(self.price-self.amount)
        else:
            self.stock-=1
            change=self.amount-self.price
            self.amount=0
            if change==0:
                return 'Here is your %s.' %self.name
            else:
                return 'Here is your %s and $%i change.' %(self.name, change)



# Q2.

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    
    def __init__(self, other_class):
        self.other_class=other_class

    def ask(self, input ,*args):
        args_list=list(args)
        words=list(input.split())
        if words[0]=='please':
            if words[1]=='restock':
                return self.other_class.restock(args_list[0])
            elif words[1]=='vend':
                return self.other_class.vend()
            elif words[1]=='deposit':
                return self.other_class.deposit(args_list[0])
            else: 
                command=' '.join(words[1:])
                return 'Thanks for asking, but I know not how to %s' %command
        else:
            return 'You must learn to say please first.'





# Q3.

from life import life

class life_lists(life):
    """An implementation of the Game of Life where the board is represented
    as a list of lists, one list per row.  The elements of the row lists
    are integers; odd integers represent cells with living organisms, and
    even integers represent empty cells."""

    def __init__(self, nrows, ncols, init=None):
        """A new Life board containing NROWS rows and NCOLS columns, which wrap around.
        If INIT is not None, then it should be a sequence (any iterable) of rows, each
        of which is itself a sequence (any iterable).   The values fill the board as
        for life.set_board."""
        super().__init__(nrows, ncols)
        self._board = [[0 for c in range(ncols)] for r in range(nrows)]
        if init is not None:
            self.set_board(init)


    def _is_alive(self, row, col): #current state

        if self._board[row][col] == '*':
            return True
        else:
            return False

    def _set_alive(self, row, col, alivep): #next state

        num_neighbors = self.neighbors(row, col)
        if self._is_alive == True:   
            if num_neighbors < 2:
                self._is_alive = '-'
            elif 2 <= num_neighbors <= 3:
                self._is_alive = '*'
            elif num_neighbors > 3:
                self._is_alive = '-'
        else:
            if num_neighbors == 3:
                self._is_alive = '*'



    def tick(self):
        """Update the board to the next generation.
        >>> b = life_lists(10, 10,    # Glider
        ...                ("     ",
        ...                 "  *  ",
        ...                 "   *  ",
        ...                 " ***  ",
        ...                 "      "))
        >>> print(b, end="")
        ----------
        --*-------
        ---*------
        -***------
        ----------
        ----------
        ----------
        ----------
        ----------
        ----------
        >>> b.tick()
        >>> print(b, end="")
        ----------
        ----------
        -*-*------
        --**------
        --*-------
        ----------
        ----------
        ----------
        ----------
        ----------
        >>> b.tick()
        >>> b.tick()
        >>> b.tick()
        >>> print(b, end="")
        ----------
        ----------
        ---*------
        ----*-----
        --***-----
        ----------
        ----------
        ----------
        ----------
        ----------
        """
        
        self._board = self._is_alive._set_alive






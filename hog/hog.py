# Rebecca Lambert, Sung Hyun Woo

"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

# Taking turns

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    
    n=1
    dice_sum=0
    pig_out=0
    while n<=num_rolls:
        result=dice()
        n+=1
        dice_sum+=result 
        if result==1:
            pig_out = 1     # pig_out variable allows the function to roll num_rolls of times even if it encounters 1
    if pig_out == 1:
        return 1            #pig out rule
    else:
        return dice_sum


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    
    n=0     # variable for while comparison
    dice_sum=0
    while n<num_rolls:
        result=dice()  # result is assigned each result for reference later
        n+=1
        dice_sum+=result 
        if result==1:   # pig out rule
            dice_sum=1
            n=num_rolls+1
    if num_rolls==0:
        a=opponent_score//10        #getting the ten's place
        b=opponent_score-(10*a)     #gettting the one's place
        if a>b:
            dice_sum=a+1
        else:
            dice_sum=b+1
    return dice_sum



# Playing a game

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    if (score+opponent_score)%7==0:
        return four_sided
    else:
        return six_sided


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    score, opponent_score = 0, 0
    while score<goal and opponent_score<goal:
        dice=select_dice(score, opponent_score)

        if who==0:     # current player
            num_rolls=strategy0(score, opponent_score)
            dice_sum=take_turn(num_rolls, opponent_score, dice)
            score+=dice_sum
        elif who==1:   # opponent
            num_rolls=strategy1(opponent_score, score)
            dice_sum=take_turn(num_rolls, score, dice)
            opponent_score+=dice_sum  
                      
        who=other(who)   # switches player after each turn

        if score==(2*opponent_score):  # swap rule
            opponent_score, score = score, opponent_score
        elif opponent_score==(2*score):
            score, opponent_score = opponent_score, score
    return score, opponent_score  



#######################
# Phase 2: Strategies #
#######################

# Basic Strategy


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    def take_average(*args):
        sum=0
        n=0
        while n<num_samples:
            sum+=fn(*args)     #calls the function *args number of times and adds onto sum
            n+=1
        return sum/num_samples
    return take_average


def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Print all averages as in
    the doctest below.  Assume that dice always returns positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    1 dice scores 3.0 on average
    2 dice scores 6.0 on average
    3 dice scores 9.0 on average
    4 dice scores 12.0 on average
    5 dice scores 15.0 on average
    6 dice scores 18.0 on average
    7 dice scores 21.0 on average
    8 dice scores 24.0 on average
    9 dice scores 27.0 on average
    10 dice scores 30.0 on average
    10
    """
    cur_dice = 1   # current number of dice
    max_avg= 0     # maximum average so far
    max_dice=0     # maximum scoring number of dice
    while cur_dice<=10:
        current_avg= make_averaged(roll_dice, 1000)(cur_dice, dice)
        if current_avg >max_avg:
            max_avg=current_avg
            max_dice= cur_dice
        cur_dice +=1
    return max_dice


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if True: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """

    a=opponent_score//10
    b=opponent_score-(10*a)
    if a>= margin -1 or b>= margin -1:
        return 0
    else:
        return num_rolls

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it would result in a beneficial swap and
    rolls NUM_ROLLS if it would result in a harmful swap. It also rolls
    0 dice if that gives at least MARGIN points and rolls
    NUM_ROLLS otherwise.
    """
    if score < opponent_score:
        if opponent_score>(score + margin):
            return 0
        else:
            return num_rolls
    else:
        return num_rolls
  

def final_strategy(score, opponent_score):
    """
    Our final strategy was designed by organizing priorities and return
    the number of dice depending whether or not it satisfies certain
    conditions. The first priority that the code checks is whether or not 
    the current player is 10 points or less away from winning and uses the 
    bacon strategy depending on its condition. The second examines the scores 
    and see if it is possible to take advantage of the hog wild rule. The 
    third check sees how much risk the player should take depending on how 
    much the player is leading by. The last check examines if the player is 
    winning or losing, and gives conditions for the bacon rule. If none of 
    the conditions are satisfied, the default number of dice is 6.

    """

# check 1

    if (100-score) <= 10:     # when 10 points away from 100,take advantage of the bacon rule
        a=opponent_score//10           
        b=opponent_score-(10*a)
        if (score+ max(a, b)) >= 100:
            return 0
        if (score+opponent_score)%7 ==0:
            if bacon_strategy(score, opponent_score, 6, 6) ==0:
                return 0
        if opponent_score>score:
            return 5
        else:
            return 6

# check 2

    if (score+opponent_score)%7 ==0:
        if bacon_strategy(score, opponent_score, 6, 6) ==0:
            return 0
        else:
            return 3

# check 3

    if score < opponent_score:
        if select_dice == four_sided:
            return 2
        if opponent_score>(score + 10):        
            return 7
        else: 
            return 6

# check 4

    if score-opponent_score>=10:
        if bacon_strategy(score, opponent_score, 8, 6)==0:
            return 0
        else: 
            return 5
    elif opponent_score-score>=10:
        if bacon_strategy(score, opponent_score, 8, 7)==0:
            return 0
        else:
            return 7
    else:
        if select_dice==four_sided:
            return 2
        elif score >= (opponent_score-5):
            return 6
        else:
            return 6





##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()

# 1st
def wins_rock_scissors_paper(player_throw, opponent_throw):
    player_throw = player_throw.lower()
    opponent_throw = opponent_throw.lower()
    rules = {
        'scissors': 'paper',
        'paper': 'rock',
        'rock': 'scissors'
    }
    if rules[player_throw] == opponent_throw:
        return True
    if player_throw == opponent_throw:
        return False
    return False

#2nd ans
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#I made the function recursive because for the current scenario using recursion to make a function requires less coding and is easier to develop

#3rd ans
def Fibonacci(n):
    if n <= 0:
        return "Error.number should not be negative or 0"

    elif n == 1:
        return 1

    elif n == 2:
        return 1

    else:
        a, b = 1, 1
        for n in range(2, n):
            a, b = b, a + b
        return b
#used implementation method for the following function

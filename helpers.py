"""helpers.py has some amazing functions etc."""

def ultimate_answer(question):
    """Provides an answer to the ultimate question.

    Returns '42' if the question is 'What is the meaning of Life, The Universe,
    Everything?' otherwise returns 'That is not much of a question'
    
    args:
        question (str): The question to be answered.
        
    returns:
        str
    """

    if question == "What is the meaning of Life, The Universe, Everything?":
        answer = "42"

    else:
        answer = "That is not much of a question"

    return answer

## binary selection ##
def check_guess_bin(guess, target):
    """Checks a guess to see if it is the same as the target.

    Complete this  function using binary selection 

    Args:
        guess: int - the guessed number
        target: int - the correct or target number

    Returns:
        winner: bool - True if correct guess otherwise false

    """
    
    if guess == target:
        return True
    else:
        return False

## multiway selection
def check_guess_multi(guess, target):
    """Checks a guess to see if it is the same as the target.

    If the guess is incorrect, prompts the player to guess higher
    or lower as appropriate.

    Complete this  function using multi-way selection 

    Args:
        guess: int - the guessed number
        target: int - the correct or target number

    Returns:
        prompt: str - "higher", "lower" or "correct"

    """
    while guess != target:
        if guess > target:
            guess = int(input("Lower: "))
        else:
            guess = int(input("Higher: "))

    print("Correct")

## pre-test repetition
def factorial(num):
    """Calculates the factorial of a number.

    Use pre-test repetition to write a function that computes the factorial of a number.
    A factorial of a number is the product of all the positive integers
    less than it.
    For example 4 factorial is 4 x 3 x 2 x 1 = 24 

    Args:
        num: int - the number for which to calculate the factorial
        
    Returns:
        fact: the factorial of num
    """
    
    iteration = 0
    fact = 1

    while iteration < num:
        for i in range(1,num+1):
            iteration = iteration + 1
            fact = fact * i
        return fact

## counted repetition
def add_array(in_array):
    """Adds the elements of an array.

    Use counted repetition, using a start, finish and a step, to sum the
    elements of an array

    Args:
        in_array: array if numbers to be added

    Returns:
        sum: the sum of the array
    """
    
    sum = 0

    for i in range(0, len(in_array)):
        sum = sum + in_array[i]

    return sum

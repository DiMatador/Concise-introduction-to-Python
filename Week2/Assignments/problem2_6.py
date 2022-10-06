import random
def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    random.seed(431)
    for roll in range(0, 100):
        diceRoll = (random.randint(1, 6) + random.randint(1, 6))
        print(diceRoll)
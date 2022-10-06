import random
rolls = []
def problem2_4():
    random.seed(70)
    for i in range(0, 10):
        rolling = (5 * random.random() + 30)
        rolls.append(rolling)
    print(rolls)                           

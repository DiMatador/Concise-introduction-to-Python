'''create a list of temperatures with a range 0 to 20  with temp 20-95F and print out just 20'''

import statistics
import random

random.seed(77) # random seed
temperatures = list() # empty list to add the temps to it

def temp_stats(temps):  

    for temp in range(0, 20): # generate 20 different temps
        temperatures.append(random.randint(20, 95)) # temp between 20f and 95f, in int form

    print('\nList of Temperatures')
    print(f'{temps}')
    print()
    print(f'The Mean of temperatures is: {statistics.mean(temperatures):>18}')
    print(f'The Median of temperatures is: {statistics.median(temperatures):>16}')

    try:
        '''if this is not going to work we would do it like this '''
        # print('Mode:',statistics.mode(temperatures:>16))
        print(f'The Mode of temperatures is: {statistics.mode(temperatures):>16}')
    except statistics.StatisticsError as e:
        print('Mode Error: ', e)

    print(f'The Standard Deviation of temperatures is: {statistics.stdev(temperatures)}')
    print(f'The Variance of temperatures is: {statistics.variance(temperatures):>28}')


temp_stats(temperatures)
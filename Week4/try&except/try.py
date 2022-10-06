'''USING DESCRIPTIVE STATISTICS;  TRY/EXCEPT ERROR HANDLING\
    Example: Cumpute the statistics for the following list'''

import random
import statistics


ilis = [3, 1, 5, 2, 1, 3, 7, 3]
stat_list = list()

'''Here stat_list is gonna have 100 sudo random number between 0 - 100 with range 5000 to 6000'''
for i in range(0, 100):
    stat_list.append(1000 * random.random() + 5000)

print(stat_list)
print(ilis, end=' ')

print('\n----------------------------------------------------------------------------------------') # create space


'''Now create a function to calculate the Mean, Median, Mode, Standar Deviation and Variance'''

def my_stats(somelist):
    print(f'\nMean :{statistics.mean(somelist)}')
    print(f'Median :{statistics.median(somelist)}')
#if there is gonna be an error is gonna happen with mode: Note that python has corrected this error on later updates by returning one answer instead of two
    try:
        print(f'Mode :{statistics.mode(somelist)}')
    except statistics.StatisticsError as e:
        print('Mode Error: ', e)
        
    print(f'Standar Deviation :{statistics.stdev(somelist)}')
    print(f'Variance :{statistics.variance(somelist)}')

my_stats(stat_list)

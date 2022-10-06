'''USING DESCRIPTIVE STATISTICS; TRY/EXCEPT ERROR HANDLEING
Example: Compute the statistics for the following list'''
'''First lets generate a 100 random reals between 5000 and 6000'''

import random

from numpy import average


# stat_list = []

# for i in range(0, 100):
#     stat_list.append(1000 * random.random() + 5000)# 1000 will create a random number from 0-1000 when we add 5000 now we have a random number between 0-6000
# # print(stat_list)

# ilis = [3, 1, 5, 2, 1, 3, 7, 3]

# '''ilis = mean, median, mode'''
# def my_stats(somehtinH):
#     import statistics
#     print(f'Mean: {statistics.mean(somehtinH)}')
#     print('--'*20)
#     print(f'Median: {statistics.median(somehtinH)}')
#     print('--'*20)
#     print(f'Mode: {statistics.mode(somehtinH)}')
#     print('--'*20)
#     print(f'Standard Deviation: {statistics.stdev(somehtinH)}')
#     print('--'*20)
#     print(f'Variance: {statistics.variance(somehtinH)}')
#     print()  
# my_stats(stat_list)
# print('--' * 20)

'''--------------------------------------------------------------------------'''

'''TRY and EXCEPT'''
def test_try():
    num = input('Enter a Number: ')
    print(type(num))
    try:
        numf = float(num)
        print(numf)
    except Exception as e:
        print('Exception was: ', e)
test_try()

print('--' * 20)

'''-------------------------------------------------------------------------'''

'''exercise 4.1... error handling'''

random.seed(277)# now is 77.... change to 277 and see what happends
temperature = []
ct = 0

for temp in range(0, 20):
    temperature.append(random.randint(20, 95))
    ct+=1
    average = temp / ct

print(temperature, end=', ')

print('\n----------------------------------------------------')

'''perform stats on the temperatures'''
def temp_stat(temps):
    import statistics
    print(f'Mean is: {statistics.mean(temps)}')
    print(f'Median is: {statistics.median(temps)}')
    print(f'Standard Deviation: {statistics.stdev(temps)}')
    print(f'Variance is: {statistics.variance(temps)}')
    try:
        print(f'Mode is: {statistics.mode(temps)}')
    except Exception as e:
        print('Mode Error: ', e)
    print(f'Average is: {average}')

temp_stat(temperature)



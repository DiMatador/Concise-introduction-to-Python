import statistics

nlist = [2, 4, 13, 3, 7, 8, 5]
nlisteven = nlist + [9]
rlist = [3.14, 2.71, -8.43, 5.25, 10.11, -23.78, 44.45 ]
rlisteven = rlist + [90.3]
'''Standar diviation is the square root of the variance. both standard diviation and variance\
     measure how spread out the data is '''

print('Standard Diviation measures how spread out data is, the same for variance')
print(f'The standar diviation for nlist is: {statistics.stdev(nlist)}')
print(f'The standard diviation for nlisteven is: {statistics.stdev(nlisteven)}')
print(f'The standard diviation for rlist is: {statistics.stdev(rlist)}')
print(f'The standard diviation for rlisteven is: {statistics.stdev(rlisteven)}'

)
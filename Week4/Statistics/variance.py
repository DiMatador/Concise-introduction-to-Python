import statistics

nlist = [2, 4, 13, 3, 7, 8, 5]
nlisteven = nlist + [9]
rlist = [3.14, 2.71, -8.43, 5.25, 10.11, -23.78, 44.45 ]
rlisteven = rlist + [90.3]


print(f'The variance of nlist is: {statistics.variance(nlist)}')
print(f'The variance of nlisteven is: {statistics.variance(nlisteven)}')
print(f'The variance of rlist is: {statistics.variance(rlist)}')
print(f'The variance of rlisteven is: {statistics.variance(rlisteven)}')

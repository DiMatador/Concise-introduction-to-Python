import statistics

nlist = [2, 4, 13, 3, 7, 8, 5]
nlisteven = nlist + [9]
rlist = [3.14, 2.71, -8.43, 5.25, 10.11, -23.78, 44.45 ]
rlisteven = rlist + [90.3]

print(f'The mean for nlist is: {statistics.mean(nlist)}')
print(f'The mean for nlisteven is: {statistics.mean(nlisteven)}')
print(f'The mean for rlist is: {statistics.mean(rlist)}')
print(f'The mean for rlisteven is: {statistics.mean(rlisteven)}')



import statistics

nlist = [2, 4, 13, 3, 7, 8, 5]
nlisteven = nlist + [9]
rlist = [3.14, 2.71, -8.43, 5.25, 10.11, -23.78, 44.45]
rlisteven = rlist + [90.3]

# Find the mean or nlist
statistics.mean(nlist)
print(statistics.mean(nlist))
# Find the mean of rlist
statistics.mean(rlist)
print(statistics.mean(rlist))

print()

# Sort nlist
print(f'enlist {nlist}')
print(f'forted nlist: {nlist}')

print()
# Print sorted version of nlisteven to see median
print(f'nlisteven {nlisteven}')
print(f'Sorted nlisteven {sorted(nlisteven)}')

print()

# rlist and rlist sorted
print(f'rlist: {rlist}')
print(f'rlist sorted: {sorted(rlist)}')

print()

# rlist median
statistics.median(rlisteven)
print(f'rlisteven median: {statistics.median(rlisteven)}')

print()

mlist = [2, 3, 4, 5, 4, 5, 3, 6, 1, 3, 4, 3]
# sorted version of mlist
print(f'mlist: {mlist}')
print(f'sorted mlist: {sorted(mlist)}')

print()

'''Mode = is the value that accourse more often'''
print(f'Mode of mlist: {statistics.mode(mlist)} , Note: the value that appears the most is " 3 "')
# standar diviation
print(f'rlist in standard diviation: {statistics.stdev(rlist)}')
# Vatiance
print(f'rlist in variance: {statistics.variance(rlist)}')

print()


'''list functions ---- max, min, sum ------'''
nlis = [3.14, -4, 25, 8, 106, 32]
print(f'nlist: {nlis}')
print(f'The maximum of nlis is: {max(nlis)}')
print(f'The minimum of nlis is: {min(nlis)}')
print(f'The sum of nlis is: {sum(nlis)}')

print()


import statistics

nlist = [2, 4, 13, 3, 7, 8, 5]
nlisteven = nlist + [9]
rlist = [3.14, 2.71, -8.43, 5.25, 10.11, -23.78, 44.45 ]
rlisteven = rlist + [90.3]

print(f'nlist sorted ==> {sorted(nlist)} The mode for nlist is: {statistics.mode(nlist)}')
print(f'nlisteven sorted ==> {sorted(nlisteven)} The mode for nlisteven is: {statistics.mode(nlisteven)}')
print(f'rlist sorted ==> {sorted(rlist)} The mode for rlist is: {statistics.mode(rlist)}')
print(f'rlisteven sorted ==> {sorted(rlisteven)} The mode for rlisteven is: {statistics.mode(rlisteven)}')

'''Find the Mode.... Mode = the value that accourse most often'''
mlist = [2, 3, 4, 5, 4, 5, 3, 6, 1, 3, 4, 3,]
'''this mite crash!!!!'''
print(f'mlist sorted ==> {sorted(mlist)} The mode mlist is: {statistics.mode(mlist)}')

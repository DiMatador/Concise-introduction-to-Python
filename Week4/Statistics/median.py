import statistics

nlist = [2, 4, 13, 3, 7, 8, 5]
nlisteven = nlist + [9]
rlist = [3.14, 2.71, -8.43, 5.25, 10.11, -23.78, 44.45 ]
rlisteven = rlist + [90.3]

print(f'nlist sorted ==> {sorted(nlist)} The mediam for nlist is: {statistics.median(nlist)}')
print(f'nlisteven sorted ==> {sorted(nlisteven)} The median for nlisteven is: {statistics.median(nlisteven)}')
print(f'rlist sorted ==> {sorted(rlist)} The median for rlist is: {statistics.median(rlist)}')
print(f'rlisteven sorted ==> {sorted(rlisteven)} The median for rlisteven is: {statistics.median(rlisteven)}')

print('hello')

for i in range(10,20):
    print(i, end=' ')    
print('\nbye')

nums= [1,7,3,6,5,6]
sums=[]
sums.append(nums[0])
for i in range(len(nums)):
    sums.append(sums[i-1]+nums[i])
print(sums)
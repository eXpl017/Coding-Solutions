nums = [2,7,11,15]
target = 18
n = len(nums)

nums.sort()

'''
i = 0
j = 1
while (i < n-1 and j < n):
	if(nums[i] + nums[j] == target):
		print(i,j)
		break
	elif(nums[i] + nums[j] < target):
		j += 1
	else:
		print("no such nums")
		break
'''

for i in range(n-1):
	for j in range(i+1,n):
		if(nums[i] + nums[j] == target):
			print(i,j)
			break
		elif(nums[i] + nums[j] < target):
			continue
		else:
			print("no such numbers")
			break
	else:
		continue
	break
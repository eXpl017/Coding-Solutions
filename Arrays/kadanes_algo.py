def maxsubarray(arr):
	global lookup
	n = len(arr)
	localmax = 0

	for i in range(n-1, 0, -1):
		localmax = max(arr[i],arr[i]+localmax)
		lookup[i] = localmax

arr = [-2,1,-3,4,-1,2,1,-5,4]
lookup = [0]*len(arr)
maxsubarray(arr)
print(max(lookup))
def findele(arr):
	n = len(arr)
	localmin = 100
	localmax = -100
	left = [0]*n
	right = [0]*n
	for i in range(n-1,0,-1):
		if arr[i] < localmin:
			localmin = arr[i]
		left[i] = localmin
	print(left)

	for i in range(n):
		if arr[i] > localmax:
			localmax = arr[i]
		right[i] = localmax
	print(right)

	for i in range(len(left)):
		if left[i] == right[i]:
			print(left[i])
			break

arr = [5,1,4,3,6,8,10,7,9]
findele(arr)
def maxactivities(arr,n):
	#sorting
	arr.sort(key = lambda x : x[1])

	#print(arr)

	i = arr[0]
	solution = [i]
	for j in range(1,n):
		if arr[j][0] > i[1]:
			solution.append(arr[j])
			i = arr[j]
	print(solutio)

Activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
n = len(Activity)
selected = maxactivities(Activity,n)
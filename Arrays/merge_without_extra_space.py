def sorting(arr1,arr2):
	for i in range(len(arr2)):
		for j in range(len(arr1)):
			if arr1[j] > arr2[i]:
				t = arr1[j]
				arr1[j] = arr2[i]
				arr2[i] = t

	arr1.sort()
	arr2.sort()

arr1 = [1,4,7,8,10]
arr2 = [2,3,9]
sorting(arr1,arr2)
print(arr1)
print()
print(arr2)
def intersection(arr1,arr2):
	arr1.sort()
	arr2.sort()
	print(arr1,arr2)
	common = []
	i=j=0
	while(i < len(arr1) and j < len(arr2)):
		if arr1[i] == arr2[j]:
			common.append(arr1[i])
			i += 1
			j += 1
		elif arr1[i] < arr2[j]:
			i += 1
		else:
			j += 1
	return common

arr1 = [1,2,2,1]
arr2 = [2,2]
a = intersection(arr1,arr2)
print(a)
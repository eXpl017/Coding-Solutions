def minpathsum(triangle):
	k = 0
	minsum = triangle[0][0]
	for i in range(1,len(triangle)):
		if (triangle[i][k] > triangle[i][k+1]):
			minsum += triangle[i][k+1]
			k += 1
			#print(minsum)
		else:
			minsum += triangle[i][k]
			#print(minsum)
	print(minsum)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
minpathsum(triangle)
coins = [1,2,5,10,20,50,100,500,1000]
coins.sort(reverse=True)
count = 0
n = int(input("enter number: "))

def mincoins(n):
	global count
	if n == 0:
		print(count)
	else:
		for i in coins:
			if (n >= i):
				n -= i
				count += 1
				print("count: {} and number: {}".format(count,i))
				mincoins(n)
				break

mincoins(n)
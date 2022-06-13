print("enter board size: ")
n = int(input())
sol = [[0 for i in range(n)] for j in range(n)]
print(sol)
pos = 1
xmove = [1,1,2,2,-1,-1,-2,-2]
ymove = [-2,2,-1,1,-2,2,-1,1]

def isvalid(x, y):
	return (x>0 and y>0 and x<=n and y<=n)

def knightstour(sol, i, j, pos):
	sol[i][j] = pos

	if pos >= n*n:
		print(sol)
		sol[i][j] = 0
		return

	for k in range(8):
		newi = i + xmove[k]
		newj = j + ymove[k]
		if isvalid(newi, newj) and sol[newi][newj] == 0:
			knightstour(sol, newi, newj, pos+1)

	sol[i][j] = 0

knightstour(sol, 0, 0, pos)